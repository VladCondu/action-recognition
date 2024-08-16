from dataclasses import dataclass
from typing import Callable
import time

from body import Body


@dataclass
class Exercise:
    name: str
    image_url: str
    is_side_position: bool
    is_front_position: bool
    reps: int
    elapsed_time: float
    body: Body
    condition: Callable[[Body, int], bool]
    direction: int = 0

    def __post_init__(self):
        if self.is_side_position and self.is_front_position:
            raise ValueError("Exercise cannot be both side and front position")

    def check_conditions(self):
        return self.condition(self.body, self.direction)

    def give_hints(self):
        pass
