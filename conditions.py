import numpy as np


def left_side_lunge_condition(body, direction):
    percentage = np.interp(body.left_knee_angle, (170, 90), (0, 100))
    return 85 < body.left_knee_angle < 95 and 170 < body.right_knee_angle < 180


def left_elbow_bend_condition(body, direction):
    percentage = np.interp(body.right_elbow_angle, (90, 175), (0, 100))
    if percentage == 100:
        if direction == 0:
            return False, 1
    if percentage == 0:
        if direction == 1:
            return True, 0

    return False, direction
