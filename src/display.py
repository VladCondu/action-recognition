import time

import cv2
import mediapipe as mp
import numpy as np
import pygame
from pygame import gfxdraw

import exercise_sets
from body import Body
from exercise_rect import ExerciseRect
from paginator import Paginator
from utils import Utils


class Display:

    def __init__(self):
        self.cap = self.start_webcam_capture()
        self.window = pygame.display.set_mode((Utils.width, Utils.height), vsync=True)
        self.clock = pygame.time.Clock()
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.back_button_image = pygame.image.load("resources/buttons/previous.png").convert_alpha()
        self.back_button_image = pygame.transform.scale(self.back_button_image, (50, 50))
        self.hovered = pygame.image.load("resources/buttons/previous_hovered.png").convert_alpha()
        self.hovered = pygame.transform.scale(self.hovered, (50, 50))

    @staticmethod
    def start_webcam_capture():
        capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
        capture.set(cv2.CAP_PROP_FPS, 30)
        return capture

    def preview_exercise(self, exercise):
        click = False
        running = True
        gif = Utils.get_gif_from_url(exercise.gif_path, x=Utils.width / 2, y=Utils.height / 2 + 200, scale=1.5)

        while running:
            mx, my = pygame.mouse.get_pos()

            self.get_body_and_display_frame(True)

            # black overlay
            black_overlay = pygame.Surface((Utils.width, Utils.height))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            self.window.blit(black_overlay, (0, 0))

            gif.update()
            gif.draw(self.window)

            self.draw_text(exercise.name, Utils.width / 2, Utils.height - 150, 50)

            if self.draw_back_button(mx, my, click):
                running = False
                click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            pygame.display.flip()

    def pause_screen(self, remaining_time):
        click = False
        running = True
        resume_button = pygame.image.load("resources/buttons/play_button.png").convert_alpha()
        resume_button = pygame.transform.scale(resume_button, (100, 100))
        resume_hovered = pygame.image.load("resources/buttons/play_hovered.png").convert_alpha()
        resume_hovered = pygame.transform.scale(resume_hovered, (100, 100))
        resume = False

        minutes = int(remaining_time / 60)
        if minutes < 10:
            minutes = f'0{minutes}'

        seconds = int(remaining_time % 60)
        if seconds < 10:
            seconds = f'0{seconds}'

        while running:
            mx, my = pygame.mouse.get_pos()

            self.get_body_and_display_frame()
            black_overlay = pygame.Surface((Utils.width, Utils.height))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            self.window.blit(black_overlay, (0, 0))

            self.draw_text(f'Remaining time: {minutes}:{seconds}', Utils.width / 2, 400, 40)
            self.draw_text("Paused", Utils.width / 2, Utils.height / 2, 100)

            self.window.blit(resume_button, (Utils.width / 2 - 50, 620))
            if resume_button.get_rect().move(Utils.width / 2 - 50, 620).collidepoint((mx, my)):
                self.window.blit(resume_hovered, (Utils.width / 2 - 50, 620))
                if click:
                    running = False
                    resume = True
                    click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = False

            pygame.display.flip()

        return resume

    def check_if_body_in_frame(self, body, is_standing, countdown):
        if body is None:
            return False
        if is_standing:
            if (0.2 < body.nose[0] < 0.8 and 0.1 < body.nose[1] < 0.5
                    and 0.2 < body.right_heel[0] < 0.8 and 0.5 < body.right_heel[1] < 1
                    and 0.2 < body.left_heel[0] < 0.8 and 0.5 < body.left_heel[1] < 1):
                self.draw_text(f'{countdown}', Utils.width / 2, Utils.height / 2, 100)
                return True
        else:
            if (0.1 < body.nose[0] < 0.9 and 0.2 < body.nose[1] < 0.8
                    and 0.1 < body.right_heel[0] < 0.9
                    and 0.2 < body.right_heel[1] < 0.8
                    and 0.1 < body.left_heel[0] < 0.9
                    and 0.2 < body.left_heel[1] < 0.8):
                self.draw_text(f'{countdown}', Utils.width / 2, Utils.height / 2, 100)
                return True
        return False

    def draw_text(self, text, centerx, centery, font_size=50, color=Utils.WHITE_SHADE):
        font = pygame.font.Font(Utils.font, font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(centerx, centery))
        self.window.blit(text, text_rect)

    def draw_text_for_duration(self, text, x, y, size, duration, include_time=False):
        start_time = time.time()
        rect = pygame.Rect(Utils.width / 2, Utils.height / 2, 0.7 * size * len(text) * 0.9, size * 1.5)
        rect.center = (Utils.width / 2, Utils.height / 2)
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
            rect = pygame.rect.Rect(0, 0, 900, 100)
            rect.center = (Utils.width / 2, Utils.height / 2)
            pygame.draw.rect(self.window, Utils.GRAY_SHADE, rect, border_radius=10)
            font = pygame.font.Font('resources/fonts/Laro Soft Medium.ttf', 50)
            text = font.render("Go back in frame", True, Utils.BLUE_SHADE_DARK)
            text_rect = text.get_rect(center=(Utils.width / 2, Utils.height / 2))
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

    def wait_for_body_in_frame(self, exercise):
        click = False
        countdown = 5
        last_decrement_time = time.time()

        while countdown > 0:
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            body = self.get_body_and_display_frame(True)
            self.draw_get_in_frame_border(exercise.is_standing)

            image = pygame.image.load(exercise.starting_posture_path).convert_alpha()
            image.set_alpha(180)
            self.window.blit(image, (0, 0))

            rect = pygame.Rect(0, 0, 750, 70)
            if exercise.is_standing:
                self.draw_text("Stand in the box", Utils.width / 2, 80, 30)
                self.draw_text("Take your starting position", Utils.width / 2, 110, 30)
                rect.center = (Utils.width / 2, 970)
                pygame.draw.rect(self.window, Utils.BLUE_SHADE_DARK, rect, border_radius=20)
                self.draw_text(exercise.name, rect.centerx, rect.centery - 5, 50, Utils.WHITE_SHADE)
            else:
                self.draw_text("Lay down in the box", Utils.width / 2, 80, 30)
                self.draw_text("Take your starting position", Utils.width / 2, 120, 30)
                self.draw_text("Feel free to adjust the camera", Utils.width / 2, 170, 15)
                rect.center = (Utils.width / 2, 870)
                pygame.draw.rect(self.window, Utils.BLUE_SHADE_DARK, rect, border_radius=20)
                self.draw_text(exercise.name, rect.centerx, rect.centery - 5, 50, Utils.WHITE_SHADE)

            current_time = time.time()
            is_body_in_frame = self.check_if_body_in_frame(body, exercise.is_standing, countdown)
            if is_body_in_frame and current_time - last_decrement_time >= 1:
                countdown -= 1
                last_decrement_time = current_time
                print(f'Countdown: {countdown}')
            elif not is_body_in_frame:
                countdown = 5

            if self.draw_back_button(mx, my, click):
                return False
            pygame.display.flip()

        return True

    def draw_exercise_hud(self, exercise, percentage, gif, remaining_time, mx, my, click):
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

        pygame.gfxdraw.filled_circle(self.window, 1120, 150, 100, Utils.BLUE_SHADE_BRIGHT)
        pygame.draw.arc(self.window, Utils.BLUE_SHADE_DARK, (1020, 50, 200, 200), 0,
                        3.1415 * (1 - percentage / 100), 20)
        pygame.gfxdraw.filled_circle(self.window, 1120, 150, 80, Utils.GRAY_SHADE)
        pygame.draw.rect(self.window, Utils.GRAY_SHADE, (990, 150, 260, 110))

        self.draw_text(f'{exercise.reps}', 1120, 150, 72, Utils.WHITE_SHADE)
        self.draw_text(f'{minutes}:{seconds}', 1120, 260, 45, Utils.WHITE_SHADE)

        pause_button = pygame.image.load("resources/buttons/pause_button.png").convert_alpha()
        pause_button = pygame.transform.scale(pause_button, (50, 50))
        pause_hovered = pygame.image.load("resources/buttons/pause_hovered.png").convert_alpha()
        pause_hovered = pygame.transform.scale(pause_hovered, (50, 50))

        self.window.blit(pause_button, (50, 120))
        if pause_button.get_rect().move(50, 120).collidepoint((mx, my)):
            self.window.blit(pause_hovered, (50, 120))
            if click:
                return True

        pygame.display.flip()

    def draw_back_button(self, mx, my, click):
        self.window.blit(self.back_button_image, (50, 50))
        if self.back_button_image.get_rect().move(50, 50).collidepoint((mx, my)):
            self.window.blit(self.hovered, (50, 50))
            if click:
                return True

    def build_your_own_set(self):
        click = False
        running = True
        items_per_page = 9
        paginator = Paginator(exercise_sets.exercise_list, items_per_page)
        total_pages = paginator.total_pages()
        selected_exercises = []
        break_duration = 15
        preview_button_image = pygame.image.load("resources/buttons/preview.png").convert_alpha()
        preview_button_image = pygame.transform.scale(preview_button_image, (50, 50))
        preview_hovered = pygame.image.load("resources/buttons/preview_hovered.png").convert_alpha()
        preview_hovered = pygame.transform.scale(preview_hovered, (50, 50))

        while running:
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = False

            self.get_body_and_display_frame(False)

            black_overlay = pygame.Surface((1280, 1024))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            self.window.blit(black_overlay, (0, 0))

            self.draw_text("Build your own set", Utils.width / 2, 70, 40)

            # draw exercises
            current_page_items = paginator.get_current_page_items()
            for i, exercise in enumerate(current_page_items):
                row, col = divmod(i, 3)
                x, y = Utils.width / 2 + col * 300 - 300, 250 + row * 220
                exercise_rect = ExerciseRect(exercise)
                exercise_rect.rect.center = (x, y)

                color = Utils.BLUE_SHADE_BRIGHT if exercise in selected_exercises else Utils.GRAY_SHADE
                color = Utils.BLUE_SHADE_DARK if exercise_rect.rect.collidepoint(
                    (mx, my)) and exercise not in selected_exercises else color
                pygame.draw.rect(self.window, color, exercise_rect.rect, border_radius=20)
                self.draw_text(exercise.name, x, y, 20)

                if exercise_rect.rect.collidepoint((mx, my)) and click:
                    if exercise in selected_exercises:
                        selected_exercises.remove(exercise)
                    else:
                        selected_exercises.append(exercise)
                    click = False

                if exercise in selected_exercises:
                    reps_title_y, reps_counter_y = y + 60, y + 90
                    time_title_y, time_counter_y = y + 120, y + 150

                    self.draw_text("Reps", x + 60, reps_title_y, 20)
                    self.draw_text(str(exercise.reps), x + 60, reps_counter_y, 20)
                    self.draw_text("Time (s)", x + 60, time_title_y, 20)
                    self.draw_text(str(exercise.elapsed_time), x + 60, time_counter_y, 20)
                    self.window.blit(preview_button_image, (x - 80, y + 80))

                    reps_increase_button = pygame.Rect(x + 90, reps_counter_y - 10, 20, 20)
                    reps_decrease_button = pygame.Rect(x + 10, reps_counter_y - 10, 20, 20)
                    time_increase_button = pygame.Rect(x + 90, time_counter_y - 10, 20, 20)
                    time_decrease_button = pygame.Rect(x + 10, time_counter_y - 10, 20, 20)

                    for button, text in [(reps_increase_button, "+"), (reps_decrease_button, "-"),
                                         (time_increase_button, "+"), (time_decrease_button, "-")]:
                        button_color = Utils.BLUE_SHADE_DARK if button.collidepoint((mx, my)) else Utils.GRAY_SHADE
                        pygame.draw.rect(self.window, button_color, button)
                        self.draw_text(text, button.centerx, button.centery, 20)

                    if reps_increase_button.collidepoint((mx, my)) and click:
                        exercise.reps += 1
                        click = False
                    if reps_decrease_button.collidepoint((mx, my)) and click:
                        exercise.reps = max(1, exercise.reps - 1)
                        click = False
                    if time_increase_button.collidepoint((mx, my)) and click:
                        exercise.elapsed_time += 5
                        click = False
                    if time_decrease_button.collidepoint((mx, my)) and click:
                        exercise.elapsed_time = max(5, exercise.elapsed_time - 5)
                        click = False
                    if preview_button_image.get_rect().move(x - 80, y + 80).collidepoint((mx, my)):
                        self.window.blit(preview_hovered, (x - 80, y + 83))
                        if click:
                            self.preview_exercise(exercise)
                            click = False

            # break duration
            break_title_x, break_counter_x = 350, 350
            break_title_y, break_counter_y = 950, 980
            self.draw_text("Break pause duration (s)", break_title_x, break_title_y, 20)
            self.draw_text(str(break_duration), break_counter_x, break_counter_y, 20)

            break_increase_button = pygame.Rect(break_counter_x + 30, break_counter_y - 10, 20, 20)
            break_decrease_button = pygame.Rect(break_counter_x - 50, break_counter_y - 10, 20, 20)
            for button, text in [(break_increase_button, "+"), (break_decrease_button, "-")]:
                button_color = Utils.BLUE_SHADE_DARK if button.collidepoint((mx, my)) else Utils.GRAY_SHADE
                pygame.draw.rect(self.window, button_color, button)
                self.draw_text(text, button.centerx, button.centery, 20)

            if break_increase_button.collidepoint((mx, my)) and click:
                break_duration += 5
                click = False
            if break_decrease_button.collidepoint((mx, my)) and click:
                break_duration = max(5, break_duration - 5)
                click = False

            # paginator
            button_width, button_height, spacing = 50, 50, 10
            total_width = total_pages * button_width + (total_pages - 1) * spacing
            start_x = (1280 - total_width) // 2
            for page in range(total_pages):
                button_rect = pygame.Rect(start_x + page * (button_width + spacing), 950, button_width, button_height)
                color = Utils.BLUE_SHADE_DARK if page == paginator.current_page else Utils.GRAY_SHADE
                pygame.draw.rect(self.window, color, button_rect, border_radius=10)
                self.draw_text(str(page + 1), button_rect.centerx, button_rect.centery, 20)
                if button_rect.collidepoint((mx, my)):
                    if page != paginator.current_page:
                        pygame.draw.rect(self.window, Utils.BLUE_SHADE_BRIGHT, button_rect, border_radius=10)
                        self.draw_text(str(page + 1), button_rect.centerx, button_rect.centery, 20)
                    if click:
                        paginator.current_page = page
                        click = False

            # back button
            if self.draw_back_button(mx, my, click):
                return 0, []

            # begin set button
            begin_set_button = pygame.Rect(840, 950, 200, 50)
            if selected_exercises:
                pygame.draw.rect(self.window, Utils.GRAY_SHADE, begin_set_button, border_radius=10)
                self.draw_text("Start set", begin_set_button.centerx, begin_set_button.centery, 20)
            else:
                pygame.draw.rect(self.window, Utils.GRAY_SHADE, begin_set_button, border_radius=10)
                self.draw_text("Start set", begin_set_button.centerx, begin_set_button.centery, 20,
                               color=Utils.GRAY_SHADE_HOVER)

            if begin_set_button.collidepoint((mx, my)):
                if selected_exercises:
                    pygame.draw.rect(self.window, Utils.BLUE_SHADE_DARK, begin_set_button, border_radius=10)
                    self.draw_text("Start set", begin_set_button.centerx, begin_set_button.centery, 20)
                    if click:
                        return break_duration, selected_exercises

            pygame.display.flip()
