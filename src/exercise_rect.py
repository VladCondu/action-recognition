from exercise import Exercise
import pygame


class ExerciseRect:
    def __init__(self, exercise: Exercise):
        self.exercise = exercise
        self.rect = pygame.rect.Rect(0, 0, 280, 100)
        self.scroll_offset = 0
