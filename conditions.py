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


def left_side_lunge(body, direction):
    left_knee_percentage = np.interp(body.right_knee_angle, (100, 170), (100, 0)) * 0.80
    right_knee_percentage = np.interp(body.left_knee_angle, (174, 177), (100, 0)) * 0.20
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def left_elbow_bend(body, direction):
    percentage = np.interp(body.right_elbow_angle, (90, 175), (0, 100))
    return verify_rep(percentage, direction)


def crunches(body, direction):
    percentage = np.interp(body.right_outer_hip_angle, (55, 145), (0, 100))
    return verify_rep(percentage, direction)


def pile_squats(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (0, 100)) * 0.5
    right_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def lunges_right_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.left_knee_angle, (120, 175), (100, 0)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def lunges_left_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (120, 175), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (100, 0)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def side_lunges_left_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (100, 0)) * 0.5
    right_hip_percentage = np.interp(body.right_inner_hip_angle, (90, 120), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_hip_percentage)
    return verify_rep(percentage, direction)


def side_lunges_right_leg(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (100, 0)) * 0.5
    left_hip_percentage = np.interp(body.left_inner_hip_angle, (90, 120), (0, 100)) * 0.5
    percentage = int(right_knee_percentage + left_hip_percentage)
    return verify_rep(percentage, direction)


def squats(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (100, 0)) * 0.5
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (90, 110), (0, 100)) * 0.5
    percentage = int(right_knee_percentage + right_shoulder_percentage)
    return verify_rep(percentage, direction)


def hip_stretch_right_leg(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (45, 90), (100, 0)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 130), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def hip_stretch_left_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (45, 90), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 130), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def good_morning_stretch(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (60, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def press_up_back(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (150, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def right_leg_elevation(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (120, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def left_leg_elevation(body, direction):
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (120, 175), (100, 0))
    return verify_rep(int(left_outer_hip_percentage), direction)

