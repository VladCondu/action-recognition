import math
import time

import cv2
import mediapipe as mp
import numpy as np
import pygame
import conditions

from body import Body
from sprite import AnimatedSprite
from utils import Utils
from exercise import Exercise


def start_webcam_capture():
    capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
    capture.set(cv2.CAP_PROP_FPS, 30)
    return capture


def build_frame_and_body(cap, pose):
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        return None, None

    frame = cv2.flip(frame, 1)
    results = Utils.process_image(frame, pose)

    if results.pose_landmarks is None:
        print("Go back in frame")
        return frame, None

    landmarks = results.pose_landmarks.landmark

    body = Body(**{name: np.array([landmarks[landmark.value].x, landmarks[landmark.value].y])
                   for name, landmark in Utils.landmark_dict.items()})

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    return frame, body


def draw_get_in_frame_border(window, is_standing):
    if window is None:
        raise ValueError("Window is None")

    # Standing position frame
    standing_rect_origin_x, standing_rect_origin_y = 240, 50
    standing_rect_width, standing_rect_height = 800, 924

    # Laying position frame
    laying_rect_origin_x, laying_rect_origin_y = 50, 150
    laying_rect_width, laying_rect_height = 1180, 724

    if is_standing:
        standing_rect_sizes = (standing_rect_origin_x, standing_rect_origin_y,
                               standing_rect_width, standing_rect_height)
        pygame.draw.rect(window, (221, 221, 221, 70), standing_rect_sizes, 4,
                         border_radius=20)
    else:
        laying_rect_sizes = (laying_rect_origin_x, laying_rect_origin_y,
                             laying_rect_width, laying_rect_height)
        pygame.draw.rect(window, (221, 221, 221, 70), laying_rect_sizes, 4,
                         border_radius=20)

    return window


def check_if_body_in_frame(body, is_standing):
    if body is None:
        return False
    # print(f' Nose: {body.nose}')
    # print(f' Right heel: {body.right_heel}')
    # print(f' Left heel: {body.left_heel}')
    if is_standing:
        if (0.4 < body.nose[0] < 0.6 and 0.05 < body.nose[1] < 0.2
                and 0.4 < body.right_heel[0] < 0.6 and 0.8 < body.right_heel[1] < 0.9
                and 0.4 < body.left_heel[0] < 0.7 and 0.8 < body.left_heel[1] < 0.9):
            return True
    else:
        if (0.1 < body.nose[0] < 0.3 and 0.2 < body.nose[1] < 0.5
                and 0.6 < body.right_heel[0] < 0.75
                and 0.6 < body.right_heel[1] < 0.8):
            return True

    return False


def wait_for_body_in_frame(cap, pose, window, is_standing):
    countdown = 3
    last_decrement_time = time.time()

    while countdown > -1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return False

        body = get_body_and_display_frame(cap, pose, window)
        draw_get_in_frame_border(window, is_standing)

        # Update the display
        pygame.display.flip()

        # Start countdown if body is in frame
        current_time = time.time()
        is_body_in_frame = check_if_body_in_frame(body, is_standing)
        if is_body_in_frame and current_time - last_decrement_time >= 1:
            countdown -= 1
            last_decrement_time = current_time
            print(f'Countdown: {countdown}')
        elif not is_body_in_frame:
            countdown = 3

    return True


def start_exercise(exercise, cap, pose, window):
    timer = time.time()
    remaining_reps = exercise.reps
    animation_frame_list = AnimatedSprite.loadGIF(exercise.image_url)
    animated_sprite = AnimatedSprite(75, Utils.height, animation_frame_list)
    all_sprites = pygame.sprite.Group(animated_sprite)

    last_print_time = time.time()
    while time.time() - timer < exercise.elapsed_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()

        exercise.body = get_body_and_display_frame(cap, pose, window)

        current_time = time.time()

        if current_time - last_print_time >= 1:
            print(f'Time remaining: {math.ceil(exercise.elapsed_time - (current_time - timer))}')
            last_print_time = current_time

        completed, direction = exercise.check_conditions()
        if completed:
            remaining_reps -= 1
            print(f'Reps remaining: {remaining_reps}')
            if remaining_reps == 0:
                print('Exercise complete!')
                return

        exercise.direction = direction
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.flip()
    print('Time up!')
    return


def get_body_and_display_frame(cap, pose, window):
    frame, body = build_frame_and_body(cap, pose)

    # Uncomment to display angles
    # Utils.display_angles(frame, body)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_rgb = np.rot90(frame_rgb)
    # frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    img = pygame.surfarray.make_surface(frame_rgb).convert()
    img = pygame.transform.flip(img, True, False)
    img = pygame.transform.scale(img, (1280, 1024))
    window.blit(img, (0, 0))

    # Update the display
    # pygame.display.flip()

    # Cap the frame rate
    clock.tick(Utils.fps)
    return body


def main():
    pygame.init()
    window = pygame.display.set_mode((Utils.width, Utils.height))
    pygame.display.set_caption("MediaPipe action recognition")

    cap = start_webcam_capture()
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    running = True
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        try:
            while cap.isOpened() and running:
                body = get_body_and_display_frame(cap, pose, window)
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        print('Loading exercise...')
                        # exercise = Exercise("Side Lunges", "Resources/Woman doing Side Lunges.gif",
                        #                     False, True, False,
                        #                     5, 45.0,
                        #                     body,
                        #                     conditions.left_side_lunge_condition)
                        exercise = Exercise("Lunges right leg", "Resources/Woman doing Side Lunges.gif",
                                            False, True, True,
                                            2, 60.0,
                                            body,
                                            conditions.left_leg_elevation)
                        if not wait_for_body_in_frame(cap, pose, window, exercise.is_standing):
                            continue
                        print(f'Starting exercise: {exercise.name}')
                        print(f'You have {exercise.elapsed_time} seconds to complete {exercise.reps} reps')
                        start_exercise(exercise, cap, pose, window)

                pygame.display.flip()
        finally:
            cap.release()
            exit()


if __name__ == "__main__":
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    clock = pygame.time.Clock()
    main()
