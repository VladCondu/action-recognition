from dataclasses import dataclass
from typing import Callable
import time

from body import Body


@dataclass
class Exercise:
    name: str
    gif_path: str
    starting_posture_path: str
    is_side_position: bool
    is_standing: bool
    reps: int
    elapsed_time: float
    body: Body
    condition: Callable[[Body, int], bool]
    direction: int = 0

    def __post_init__(self):
        if not self.is_side_position and not self.is_standing:
            raise ValueError("Front position exercises must be standing")

    def check_conditions(self):
        if self.body is None:
            return False, self.direction, 0
        return self.condition(self.body, self.direction)

    def give_hints(self):
        pass
