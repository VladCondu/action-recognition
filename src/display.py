import time

import cv2
import mediapipe as mp
import numpy as np
import pygame
from pygame import gfxdraw

from body import Body
from utils import Utils

click = False


class Display:
    def __init__(self):
        self.cap = self.start_webcam_capture()
        self.window = pygame.display.set_mode((Utils.width, Utils.height), vsync=True)
        self.clock = pygame.time.Clock()
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    @staticmethod
    def start_webcam_capture():
        capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
        capture.set(cv2.CAP_PROP_FPS, 30)
        return capture

    def check_if_body_in_frame(self, body, is_standing, countdown):
        if body is None:
            return False
        if is_standing:
            if (0.4 < body.nose[0] < 0.6 and 0.05 < body.nose[1] < 0.2
                    and 0.4 < body.right_heel[0] < 0.6 and 0.8 < body.right_heel[1] < 0.9
                    and 0.4 < body.left_heel[0] < 0.7 and 0.8 < body.left_heel[1] < 0.9):
                self.draw_text(f'{countdown}', 640, 512, 100)
                return True
        else:
            if (0.1 < body.nose[0] < 0.3 and 0.2 < body.nose[1] < 0.5
                    and 0.6 < body.right_heel[0] < 0.75
                    and 0.6 < body.right_heel[1] < 0.8):
                self.draw_text(f'{countdown}', 640, 512, 100)
                return True
        return False

    def draw_text(self, text, x, y, font_size=50, color=Utils.WHITE_SHADE):
        font = pygame.font.Font(Utils.font, font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.window.blit(text, text_rect)

    def draw_text_for_duration(self, text, x, y, size, duration, include_time=False):
        start_time = time.time()
        rect = pygame.Rect(640, 512, 0.7 * size * len(text) * 0.9, size * 1.5)
        rect.center = (640, 512)
        while time.time() - start_time < duration:
            self.get_body_and_display_frame()
            pygame.draw.rect(self.window, Utils.GRAY_SHADE, rect, border_radius=20)
            if include_time:
                remaining_time = int(duration - (time.time() - start_time))
                self.draw_text(f'{text}{remaining_time}', x, y, size)
            else:
                self.draw_text(text, x, y, size)
            pygame.display.flip()

    def build_frame_and_body(self, draw_landmarks=False):
        success, frame = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            return None, None

        frame = cv2.flip(frame, 1)
        results = Utils.process_image(frame, self.pose)

        if results.pose_landmarks is None:
            return frame, None

        landmarks = results.pose_landmarks.landmark

        body = Body(**{name: np.array([landmarks[landmark.value].x, landmarks[landmark.value].y])
                       for name, landmark in Utils.landmark_dict.items()})

        if results.pose_landmarks and draw_landmarks:
            self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        return frame, body

    def get_body_and_display_frame(self, draw_landmarks=False):
        frame, body = self.build_frame_and_body(draw_landmarks)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = np.rot90(frame_rgb)

        img = pygame.surfarray.make_surface(frame_rgb).convert()
        img = pygame.transform.flip(img, True, False)
        img = pygame.transform.scale(img, (1280, 1024))
        self.window.blit(img, (0, 0))
        if body is None and draw_landmarks is True:
            print(draw_landmarks)
            rect = pygame.rect.Rect(0, 0, 900, 100)
            rect.center = (640, 512)
            pygame.draw.rect(self.window, Utils.GRAY_SHADE, rect, border_radius=10)
            font = pygame.font.Font('../resources/fonts/Laro Soft Medium.ttf', 50)
            text = font.render("Go back in frame", True, Utils.ORANGE_SHADE_DARK)
            text_rect = text.get_rect(center=(640, 512))
            self.window.blit(text, text_rect)
        self.clock.tick(Utils.fps)
        return body

    def draw_get_in_frame_border(self, is_standing):
        if self.window is None:
            raise ValueError("Window is None")

        standing_rect_origin_x, standing_rect_origin_y = 240, 50
        standing_rect_width, standing_rect_height = 800, 924

        laying_rect_origin_x, laying_rect_origin_y = 50, 150
        laying_rect_width, laying_rect_height = 1180, 724

        if is_standing:
            standing_rect_sizes = (standing_rect_origin_x, standing_rect_origin_y,
                                   standing_rect_width, standing_rect_height)
            pygame.draw.rect(self.window, (221, 221, 221, 70), standing_rect_sizes, 4,
                             border_radius=20)
        else:
            laying_rect_sizes = (laying_rect_origin_x, laying_rect_origin_y,
                                 laying_rect_width, laying_rect_height)
            pygame.draw.rect(self.window, (221, 221, 221, 70), laying_rect_sizes, 4,
                             border_radius=20)

    def wait_for_body_in_frame(self, is_standing, is_side_position, starting_posture_path):
        countdown = 3
        last_decrement_time = time.time()

        while countdown > -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            body = self.get_body_and_display_frame(True)
            self.draw_get_in_frame_border(is_standing)

            image = pygame.image.load(starting_posture_path).convert_alpha()
            image.set_alpha(100)
            self.window.blit(image, (0, 0))

            if is_side_position and is_standing:
                self.draw_text("Stand in the box", 640, 100, 30)
                self.draw_text("Turn towards right", 640, 130, 30)
            elif is_side_position:
                self.draw_text("Lay down, feet towards right", 640, 512, 50)

            current_time = time.time()
            is_body_in_frame = self.check_if_body_in_frame(body, is_standing, countdown)
            if is_body_in_frame and current_time - last_decrement_time >= 1:
                countdown -= 1
                last_decrement_time = current_time
                print(f'Countdown: {countdown}')
            elif not is_body_in_frame:
                countdown = 3

            # self.draw_text(f'{countdown}', 640, 512, 100)
            pygame.display.flip()

        return True

    def draw_exercise_hud(self, exercise, percentage, gif, remaining_time):
        if exercise is None:
            return

        minutes = int(remaining_time / 60)
        if minutes < 10:
            minutes = f'0{minutes}'

        seconds = int(remaining_time % 60)
        if seconds < 10:
            seconds = f'0{seconds}'

        gif.update()
        gif.draw(self.window)

        pygame.draw.rect(self.window, Utils.GRAY_SHADE, (990, 30, 260, 300), border_radius=30)

        pygame.gfxdraw.filled_circle(self.window, 1120, 150, 100, Utils.ORANGE_SHADE_DARK)
        pygame.draw.arc(self.window, Utils.ORANGE_SHADE_BRIGHT, (1020, 50, 200, 200), 0,
                        3.1415 * (1 - percentage / 100), 20)
        pygame.gfxdraw.filled_circle(self.window, 1120, 150, 80, Utils.GRAY_SHADE)
        pygame.draw.rect(self.window, Utils.GRAY_SHADE, (990, 150, 260, 110))

        self.draw_text(f'{exercise.reps}', 1120, 150, 72, Utils.WHITE_SHADE)
        self.draw_text(f'{minutes}:{seconds}', 1120, 260, 45, Utils.WHITE_SHADE)

        pygame.display.flip()
