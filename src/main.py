import logging
import math
import time
import pygame
import exercise_sets
from display import Display
from exercise_sets import sets
from utils import Utils
from exercise_rect import ExerciseRect
from paginator import Paginator

logger = logging.getLogger(__name__)


def start_exercise(exercise, display):
    click = False
    timer = time.time()
    gif = Utils.get_gif_from_url(exercise.gif_path, 1)

    # timer for printing seconds
    last_print_time = time.time()
    remaining_time = int(exercise.elapsed_time)

    while time.time() - timer < exercise.elapsed_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        exercise.body = display.get_body_and_display_frame(True)
        current_time = time.time()

        if current_time - last_print_time >= 1:
            remaining_time = math.ceil(exercise.elapsed_time - (current_time - timer))
            last_print_time = current_time

        back_button_image = pygame.image.load("../resources/previous.png").convert_alpha()
        back_button_image = pygame.transform.scale(back_button_image, (50, 50))
        display.window.blit(back_button_image, (50, 50))
        if back_button_image.get_rect().move(50, 50).collidepoint((mx, my)) and click:
            return

        completed, direction, percentage = exercise.check_conditions()
        display.draw_exercise_hud(exercise, percentage, gif, remaining_time)

        if completed:
            exercise.reps -= 1
            print(f'Reps remaining: {exercise.reps}')
            if exercise.reps == 0:
                print('Exercise complete!')
                display.draw_text_for_duration('Exercise complete!', 640, 512, 100, 3)
                return

        exercise.direction = direction

    display.draw_text_for_duration('Time up!', 640, 512, 100, 3)
    return


def begin_set(display, set_name, break_duration):
    # loading set
    exercises = sets[set_name]

    for exercise in exercises:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
        if not display.wait_for_body_in_frame(exercise):
            return
        print(f'Starting exercise: {exercise.name}')
        print(f'You have {exercise.elapsed_time} seconds to complete {exercise.reps} reps')
        start_exercise(exercise, display)
        display.draw_text_for_duration('Take a break for ', 640, 512, 100, break_duration, True)


def build_your_own_set(display):
    click = False
    running = True
    items_per_page = 9
    paginator = Paginator(exercise_sets.exercise_list, items_per_page)
    total_pages = paginator.total_pages()
    selected_exercises = []
    break_duration = 15

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

        display.get_body_and_display_frame(False)

        black_overlay = pygame.Surface((1280, 1024))
        black_overlay.set_alpha(200)
        black_overlay.fill(Utils.BLACK)
        display.window.blit(black_overlay, (0, 0))

        display.draw_text("Build your own set", 640, 70, 40)

        current_page_items = paginator.get_current_page_items()
        for i, exercise in enumerate(current_page_items):
            row, col = divmod(i, 3)
            x, y = 640 + col * 300 - 300, 250 + row * 220
            exercise_rect = ExerciseRect(exercise)
            exercise_rect.rect.center = (x, y)
            color = Utils.ORANGE_SHADE_BRIGHT if exercise in selected_exercises else Utils.ORANGE_SHADE_DARK
            pygame.draw.rect(display.window, color, exercise_rect.rect, border_radius=20)
            display.draw_text(exercise.name, x, y, 20)
            if exercise_rect.rect.collidepoint((mx, my)):
                if click:
                    if exercise in selected_exercises:
                        selected_exercises.remove(exercise)
                    else:
                        selected_exercises.append(exercise)
                    click = False

            if exercise in selected_exercises:
                reps_title_y, reps_counter_y = y + 60, y + 90
                time_title_y, time_counter_y = y + 120, y + 150

                display.draw_text("Reps", x, reps_title_y, 20)
                display.draw_text(str(exercise.reps), x, reps_counter_y, 20)
                display.draw_text("Time (s)", x, time_title_y, 20)
                display.draw_text(str(exercise.elapsed_time), x, time_counter_y, 20)

                reps_increase_button = pygame.Rect(x + 30, reps_counter_y - 10, 20, 20)
                reps_decrease_button = pygame.Rect(x - 50, reps_counter_y - 10, 20, 20)
                time_increase_button = pygame.Rect(x + 30, time_counter_y - 10, 20, 20)
                time_decrease_button = pygame.Rect(x - 50, time_counter_y - 10, 20, 20)

                for button, text in [(reps_increase_button, "+"), (reps_decrease_button, "-"),
                                     (time_increase_button, "+"), (time_decrease_button, "-")]:
                    pygame.draw.rect(display.window, Utils.GRAY_SHADE, button)
                    display.draw_text(text, button.centerx, button.centery, 20)

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

        break_title_y, break_counter_y = 880, 910
        display.draw_text("Break pause duration (s)", 640, break_title_y, 20)
        display.draw_text(str(break_duration), 640, break_counter_y, 20)

        break_increase_button = pygame.Rect(670, break_counter_y - 10, 20, 20)
        break_decrease_button = pygame.Rect(590, break_counter_y - 10, 20, 20)
        for button, text in [(break_increase_button, "+"), (break_decrease_button, "-")]:
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, button)
            display.draw_text(text, button.centerx, button.centery, 20)

        if break_increase_button.collidepoint((mx, my)) and click:
            break_duration += 5
            click = False
        if break_decrease_button.collidepoint((mx, my)) and click:
            break_duration = max(5, break_duration - 5)
            click = False

        button_width, button_height, spacing = 50, 50, 10
        total_width = total_pages * button_width + (total_pages - 1) * spacing
        start_x = (1280 - total_width) // 2
        for page in range(total_pages):
            button_rect = pygame.Rect(start_x + page * (button_width + spacing), 950, button_width, button_height)
            color = Utils.ORANGE_SHADE_DARK if page == paginator.current_page else Utils.GRAY_SHADE
            pygame.draw.rect(display.window, color, button_rect, border_radius=10)
            display.draw_text(str(page + 1), button_rect.centerx, button_rect.centery, 20)
            if button_rect.collidepoint((mx, my)) and click:
                paginator.current_page = page
                click = False

        back_button_image = pygame.image.load("../resources/previous.png").convert_alpha()
        back_button_image = pygame.transform.scale(back_button_image, (50, 50))
        display.window.blit(back_button_image, (50, 50))
        if back_button_image.get_rect().move(50, 50).collidepoint((mx, my)) and click:
            running = False
            click = False

        begin_set_button = pygame.Rect(840, 950, 200, 50)
        pygame.draw.rect(display.window, Utils.ORANGE_SHADE_DARK, begin_set_button, border_radius=10)
        display.draw_text("Start set", begin_set_button.centerx, begin_set_button.centery, 20)

        if begin_set_button.collidepoint((mx, my)) and click:
            if selected_exercises:
                sets['custom_set'] = selected_exercises
                begin_set(display, 'custom_set', break_duration)
                running = False
                click = False

        pygame.display.flip()


def main_menu():
    click = False
    pygame.init()
    display = Display()
    pygame.display.set_caption("MediaPipe action recognition")

    if not display.cap.isOpened():
        logger.error("Could not open webcam.")
        display.window.fill(Utils.BLACK)
        display.draw_text("Could not open the webcam!", 640, 462, 30)
        display.draw_text("Enable webcam and restart the application.", 640, 562, 30)
        pygame.display.flip()
        time.sleep(5)
        return

    running = True
    try:
        while display.cap.isOpened() and running:
            mx, my = pygame.mouse.get_pos()
            body = display.get_body_and_display_frame(False)

            # set buttons
            full_day_starter_set_button = pygame.Rect(640, 250, 350, 50)
            full_day_starter_set_button.center = (640, 250)
            lower_back_work_set_button = pygame.Rect(640, 350, 350, 50)
            lower_back_work_set_button.center = (640, 350)
            core_work_set_button = pygame.Rect(640, 450, 350, 50)
            core_work_set_button.center = (640, 450)
            leg_work_set_button = pygame.Rect(640, 550, 350, 50)
            leg_work_set_button.center = (640, 550)

            build_your_own_set_button = pygame.Rect(640, 600, 320, 50)
            build_your_own_set_button.center = (640, 790)

            # black overlay
            black_overlay = pygame.Surface((1280, 1024))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            display.window.blit(black_overlay, (0, 0))

            # title
            display.draw_text("Welcome to the workout app", 640, 70, 40)
            display.draw_text("Choose a workout set", 640, 150, 30)

            # draw set buttons
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, full_day_starter_set_button, border_radius=20)
            display.draw_text("Full body day starter", full_day_starter_set_button.centerx,
                              full_day_starter_set_button.centery, 30)
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, lower_back_work_set_button, border_radius=20)
            display.draw_text("Lower back work", lower_back_work_set_button.centerx, lower_back_work_set_button.centery,
                              30)
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, core_work_set_button, border_radius=20)
            display.draw_text("Core work", core_work_set_button.centerx, core_work_set_button.centery, 30)
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, leg_work_set_button, border_radius=20)
            display.draw_text("Leg work", leg_work_set_button.centerx, leg_work_set_button.centery, 30)

            # build your own set
            display.draw_text("Or", 640, 670, 30)
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, build_your_own_set_button, border_radius=20)
            display.draw_text("Build your own set", build_your_own_set_button.centerx,
                              build_your_own_set_button.centery, 30)

            # click handling
            if full_day_starter_set_button.collidepoint((mx, my)):
                if click:
                    begin_set(display, 'full_body_day_starter', 5)
                    click = False
            if lower_back_work_set_button.collidepoint((mx, my)):
                if click:
                    begin_set(display, 'lower_back_work', 15)
                    click = False
            if core_work_set_button.collidepoint((mx, my)):
                if click:
                    begin_set(display, 'core_work', 15)
                    click = False
            if leg_work_set_button.collidepoint((mx, my)):
                if click:
                    begin_set(display, 'leg_work', 15)
                    click = False
            if build_your_own_set_button.collidepoint((mx, my)):
                if click:
                    build_your_own_set(display)
                    click = False

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    running = False
                    pygame.quit()

            back_button_image = pygame.image.load("../resources/previous.png").convert_alpha()
            back_button_image = pygame.transform.scale(back_button_image, (50, 50))
            display.window.blit(back_button_image, (50, 50))
            if back_button_image.get_rect().move(50, 50).collidepoint((mx, my)) and click:
                running = False
                click = False

            pygame.display.flip()
    except Exception as e:
        logger.error(e)
    finally:
        display.cap.release()
        exit()


if __name__ == "__main__":
    main_menu()
