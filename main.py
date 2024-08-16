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
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    capture.set(cv2.CAP_PROP_FPS, 30)
    return capture


def build_frame_and_body(frame, pose):
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
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        current_time = time.time()

        if current_time - last_print_time >= 1:
            print(f'Time remaining: {int(exercise.elapsed_time - (current_time - timer))}')
            last_print_time = current_time

        completed, direction = exercise.check_conditions()
        if completed:
            remaining_reps -= 1
            print(f'Reps remaining: {remaining_reps}')
            if remaining_reps == 0:
                print('Exercise complete!')
                return

        exercise.direction = direction
        exercise.body = get_body_and_display_frame(frame, pose, window)
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.flip()


def get_body_and_display_frame(frame, pose, window):
    frame, body = build_frame_and_body(frame, pose)

    # Uncomment to display angles
    Utils.display_angles(frame, body)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_rgb = np.rot90(frame_rgb)
    # frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    img = pygame.surfarray.make_surface(frame_rgb).convert()
    img = pygame.transform.flip(img, True, False)
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
                        #                     False, True, 5, 30.0,
                        #                     body,
                        #                     conditions.left_side_lunge_condition)
                        exercise = Exercise("Elbow bends", "./Resources/Woman doing Side Lunges.gif",
                                            False, True, 5, 30.0,
                                            body,
                                            conditions.left_elbow_bend_condition)
                        print(f'Starting exercise: {exercise.name}')
                        print(
                            f'You have {exercise.elapsed_time} seconds to complete {exercise.reps} reps')
                        start_exercise(exercise, cap, pose, window)

                success, frame = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue

                body = get_body_and_display_frame(frame, pose, window)
                pygame.display.flip()
        finally:
            cap.release()
            exit()


if __name__ == "__main__":
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    clock = pygame.time.Clock()
    main()
