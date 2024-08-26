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
    timer = time.time()
    gif = Utils.get_gif_from_url(exercise.gif_path, (2 / 3))

    # timer for printing seconds
    last_print_time = time.time()
    remaining_time = int(exercise.elapsed_time)

    while time.time() - timer < exercise.elapsed_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()

        exercise.body = display.get_body_and_display_frame(True)
        current_time = time.time()

        if current_time - last_print_time >= 1:
            remaining_time = math.ceil(exercise.elapsed_time - (current_time - timer))
            last_print_time = current_time

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
        if not display.wait_for_body_in_frame(exercise.is_standing,
                                              exercise.is_side_position,
                                              exercise.starting_posture_path):
            return
        print(f'Starting exercise: {exercise.name}')
        print(f'You have {exercise.elapsed_time} seconds to complete {exercise.reps} reps')
        start_exercise(exercise, display)
        display.draw_text_for_duration('Take a break for ', 640, 512, 100, break_duration, True)


def build_your_own_set(display):
    click = False
    running = True
    items_per_page = 9  # 3x3 grid
    paginator = Paginator(exercise_sets.exercise_list, items_per_page)
    total_pages = paginator.total_pages()
    selected_exercises = []
    break_duration = 30  # Default break duration in seconds

    while running:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        display.get_body_and_display_frame(False)

        # black overlay
        black_overlay = pygame.Surface((1280, 1024))
        black_overlay.set_alpha(200)
        black_overlay.fill(Utils.BLACK)
        display.window.blit(black_overlay, (0, 0))

        # title
        display.draw_text("Build your own set", 640, 70, 40)

        # back button
        back_button_image = pygame.image.load("../resources/previous.png").convert_alpha()
        back_button_image = pygame.transform.scale(back_button_image, (50, 50))
        display.window.blit(back_button_image, (50, 50))

        current_page_items = paginator.get_current_page_items()
        for i, exercise in enumerate(current_page_items):
            row = i // 3
            col = i % 3
            x = 640 + col * 300 - 300  # Increased horizontal spacing
            y = 250 + row * 200  # Increased vertical spacing
            exercise_rect = ExerciseRect(exercise)
            exercise_rect.rect.center = (x, y)
            if exercise in selected_exercises:
                pygame.draw.rect(display.window, Utils.ORANGE_SHADE_BRIGHT, exercise_rect.rect, border_radius=20)
            else:
                pygame.draw.rect(display.window, Utils.ORANGE_SHADE_DARK, exercise_rect.rect, border_radius=20)
            display.draw_text(exercise.name, x, y, 20)
            if exercise_rect.rect.collidepoint((mx, my)) and click:
                if exercise in selected_exercises:
                    selected_exercises.remove(exercise)
                else:
                    selected_exercises.append(exercise)
                click = False

            # Display reps and time counters for selected exercises
            if exercise in selected_exercises:
                reps_title_y = y + 40
                reps_counter_y = reps_title_y + 30
                time_title_y = reps_counter_y + 30
                time_counter_y = time_title_y + 30

                display.draw_text("Reps", x, reps_title_y, 20)
                display.draw_text(str(exercise.reps), x, reps_counter_y, 20)
                display.draw_text("Time (s)", x, time_title_y, 20)
                display.draw_text(str(exercise.elapsed_time), x, time_counter_y, 20)

                # Reps increase/decrease buttons
                reps_increase_button = pygame.Rect(x + 30, reps_counter_y - 10, 20, 20)
                reps_decrease_button = pygame.Rect(x - 50, reps_counter_y - 10, 20, 20)
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, reps_increase_button)
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, reps_decrease_button)
                display.draw_text("+", reps_increase_button.centerx, reps_increase_button.centery, 20)
                display.draw_text("-", reps_decrease_button.centerx, reps_decrease_button.centery, 20)

                # Time increase/decrease buttons
                time_increase_button = pygame.Rect(x + 30, time_counter_y - 10, 20, 20)
                time_decrease_button = pygame.Rect(x - 50, time_counter_y - 10, 20, 20)
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, time_increase_button)
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, time_decrease_button)
                display.draw_text("+", time_increase_button.centerx, time_increase_button.centery, 20)
                display.draw_text("-", time_decrease_button.centerx, time_decrease_button.centery, 20)

                # Handle button clicks
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

        # Display break duration counter
        break_title_y = 850
        break_counter_y = break_title_y + 30

        display.draw_text("Break pause duration (s)", 640, break_title_y, 20)
        display.draw_text(str(break_duration), 640, break_counter_y, 20)

        # Break duration increase/decrease buttons
        break_increase_button = pygame.Rect(660, break_counter_y - 10, 20, 20)
        break_decrease_button = pygame.Rect(600, break_counter_y - 10, 20, 20)
        pygame.draw.rect(display.window, Utils.GRAY_SHADE, break_increase_button)
        pygame.draw.rect(display.window, Utils.GRAY_SHADE, break_decrease_button)
        display.draw_text("+", break_increase_button.centerx, break_increase_button.centery, 20)
        display.draw_text("-", break_decrease_button.centerx, break_decrease_button.centery, 20)

        # Handle button clicks
        if break_increase_button.collidepoint((mx, my)) and click:
            break_duration += 5
            click = False
        if break_decrease_button.collidepoint((mx, my)) and click:
            break_duration = max(5, break_duration - 5)
            click = False

        # page buttons
        button_width = 50
        button_height = 50
        spacing = 10
        total_width = total_pages * button_width + (total_pages - 1) * spacing
        start_x = (1280 - total_width) // 2
        for page in range(total_pages):
            button_rect = pygame.Rect(start_x + page * (button_width + spacing), 950, button_width, button_height)
            if page == paginator.current_page:
                pygame.draw.rect(display.window, Utils.ORANGE_SHADE_DARK, button_rect, border_radius=10)
            else:
                pygame.draw.rect(display.window, Utils.GRAY_SHADE, button_rect, border_radius=10)
            display.draw_text(str(page + 1), button_rect.centerx, button_rect.centery, 20)
            if button_rect.collidepoint((mx, my)) and click:
                paginator.current_page = page
                click = False

        if back_button_image.get_rect().move(50, 50).collidepoint((mx, my)):
            if click:
                running = False
                click = False

        begin_set_button = pygame.Rect(840, 950, 200, 50)
        pygame.draw.rect(display.window, Utils.ORANGE_SHADE_DARK, begin_set_button, border_radius=10)
        display.draw_text("Start set", begin_set_button.centerx, begin_set_button.centery, 20)

        if begin_set_button.collidepoint((mx, my)) and click:
            if len(selected_exercises) > 0:
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

            set_1_button = pygame.Rect(640, 512, 350, 50)
            set_1_button.center = (640, 512)
            set_2_button = pygame.Rect(640, 600, 320, 50)
            set_2_button.center = (640, 600)

            # black overlay
            black_overlay = pygame.Surface((1280, 1024))
            black_overlay.set_alpha(200)
            black_overlay.fill(Utils.BLACK)
            display.window.blit(black_overlay, (0, 0))

            # menu options
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, set_1_button, border_radius=20)
            display.draw_text("Full body day starter", 640, 512, 30)
            pygame.draw.rect(display.window, Utils.GRAY_SHADE, set_2_button, border_radius=20)
            display.draw_text("Build your own set", 640, 600, 30)

            # click handling
            if set_1_button.collidepoint((mx, my)):
                if click:
                    begin_set(display, 'full_body_day_starter', 10)
                    click = False
            if set_2_button.collidepoint((mx, my)):
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

            pygame.display.flip()
    except Exception as e:
        logger.error(e)
    finally:
        display.cap.release()
        exit()


if __name__ == "__main__":
    main_menu()
