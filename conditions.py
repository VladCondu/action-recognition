import numpy as np


def verify_rep(percentage, direction):
    if percentage == 100:
        if direction == 0:
            print("Half there")
            return False, 1
    if percentage == 0:
        if direction == 1:
            print("Rep completed")
            return True, 0

    return False, direction


def left_side_lunge_condition(body, direction):
    left_knee_percentage = np.interp(body.right_knee_angle, (100, 170), (100, 0)) * 0.80
    right_knee_percentage = np.interp(body.left_knee_angle, (174, 177), (100, 0)) * 0.20
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def left_elbow_bend_condition(body, direction):
    percentage = np.interp(body.right_elbow_angle, (90, 175), (0, 100))
    return verify_rep(percentage, direction)


def crunches_condition(body, direction):
    percentage = np.interp(body.right_outer_hip_angle, (55, 130), (100, 0))
    # print(int(percentage))
    return verify_rep(int(percentage), direction)


def pile_squats(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (95, 175), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (95, 175), (100, 0)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    print(percentage)
    return verify_rep(percentage, direction)
