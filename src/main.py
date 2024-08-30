import math
import time

import pygame

from display import Display
from exercise_sets import sets
from utils import Utils


def start_exercise(exercise):
    click = False
    timer = time.time()
    gif = Utils.get_gif_from_url(exercise.gif_path, scale=1)
    last_print_time = time.time()
    remaining_time = int(exercise.elapsed_time)

    while remaining_time > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = False

        mx, my = pygame.mouse.get_pos()
        exercise.body = display.get_body_and_display_frame(True)
        current_time = time.time()

        if current_time - last_print_time >= 1:
            remaining_time = math.ceil(exercise.elapsed_time - (current_time - timer))
            last_print_time = current_time

        if display.draw_back_button(mx, my, click):
            return False

        completed, direction, percentage = exercise.check_conditions()

        if display.draw_exercise_hud(exercise, percentage, gif, remaining_time, mx, my, click):
            if display.pause_screen(remaining_time):
                timer = time.time() - (exercise.elapsed_time - remaining_time)
                last_print_time = time.time()
            click = False

        if completed:
            exercise.reps -= 1
            if exercise.reps == 0:
                display.draw_text_for_duration('Exercise complete!', Utils.width / 2, Utils.height / 2, 100, 2)
                return True

        exercise.direction = direction

    display.draw_text_for_duration('Time up!', Utils.width / 2, Utils.height / 2, 100, 3)
    return True


def begin_set(set_name, break_duration):
    # loading set
    exercises = sets[set_name]

    for exercise in exercises:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
        if not display.wait_for_body_in_frame(exercise):
            return
        if start_exercise(exercise):
            display.draw_text_for_duration('Take a break for ', Utils.width / 2, Utils.height / 2, 100, break_duration,
                                           True)


def main_menu():
    click = False

    if not display.cap.isOpened():
        display.window.fill(Utils.BLACK)
        display.draw_text("Could not open the webcam!", Utils.width / 2, 462, 30)
        display.draw_text("Enable webcam and restart the application.", Utils.width / 2, 562, 30)
        pygame.display.flip()
        time.sleep(5)
        return

    running = True
    try:
        while display.cap.isOpened() and running:
            mx, my = pygame.mouse.get_pos()
            display.get_body_and_display_frame()

            buttons = [
                ("Full body day starter", 250, 'full_body_day_starter', 5),
                ("Lower back work", 350, 'lower_back_work', 15),
                ("Core work", 450, 'core_work', 15),
                ("Leg work", 550, 'leg_work', 15),
                ("Build your own set", 790, None, None)
            ]

            black_overlay = pygame.Surface((1280, 1024))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            display.window.blit(black_overlay, (0, 0))

            display.draw_text("Choose a workout set", Utils.width / 2, 150, 30)
            display.draw_text("Or", Utils.width / 2, 670, 30)

            for text, y, set_name, break_duration in buttons:
                button = pygame.Rect(Utils.width / 2, y, 350, 50)
                button.center = (Utils.width / 2, y)
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, button, border_radius=20)
                display.draw_text(text, button.centerx, button.centery, 30)

                if button.collidepoint((mx, my)):
                    pygame.draw.rect(display.window, Utils.BLUE_SHADE_DARK, button, border_radius=20)
                    display.draw_text(text, button.centerx, button.centery, 30)
                    if click:
                        if set_name:
                            begin_set(set_name, break_duration)
                        else:
                            break_duration, selected_exercises = display.build_your_own_set()
                            if selected_exercises:
                                sets['custom_set'] = selected_exercises
                                begin_set('custom_set', break_duration)
                        click = False

            if display.draw_back_button(mx, my, click):
                running = False
                click = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = False
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
                    pygame.quit()

            pygame.display.flip()
    except Exception as e:
        print(f'ERROR: {e}')
    finally:
        display.cap.release()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("FlexCam")
    display = Display()
    main_menu()
