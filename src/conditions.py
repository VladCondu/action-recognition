import numpy as np


def verify_rep(percentage, direction):
    if percentage == 100:
        if direction == 0:
            print("Half there")
            return False, 1, 50
    if percentage == 0:
        if direction == 1:
            print("Rep completed")
            return True, 0, 100

    if direction == 0:
        return False, direction, int(np.interp(percentage, (0, 100), (0, 50)))
    else:
        return False, direction, int(np.interp(percentage, (0, 100), (100, 50)))


def verify_rep_double_sided_exercises(percentage, direction):
    if percentage == 100:
        if direction == 0:
            print("1/4 there")
            return False, 1, 25
        if direction == 2:
            print("3/4 there")
            return False, 3, 75
    if percentage == 0:
        if direction == 1:
            print("half there")
            return False, 2, 50
        if direction == 3:
            print("Rep completed")
            return True, 0, 100

    if direction == 0:
        return False, direction, np.interp(percentage, (0, 100), (0, 25))
    elif direction == 1:
        return False, direction, np.interp(percentage, (0, 100), (50, 25))
    elif direction == 2:
        return False, direction, np.interp(percentage, (0, 100), (50, 75))
    else:
        return False, direction, np.interp(percentage, (0, 100), (100, 75))


def left_elbow_bend(body, direction):
    percentage = np.interp(body.right_elbow_angle, (90, 175), (0, 100))
    return verify_rep(percentage, direction)


def crunches(body, direction):
    percentage = np.interp(body.right_outer_hip_angle, (55, 145), (0, 100))
    return verify_rep(percentage, direction)


def pile_squats(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (0, 100)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def lunges_right_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (110, 175), (100, 0)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def lunges_left_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (110, 175), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (100, 0)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def side_lunges_right_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (100, 175), (100, 0)) * 0.8
    right_knee_percentage = np.interp(body.right_knee_angle, (174, 177), (100, 0)) * 0.2
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def side_lunges_left_leg(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (100, 175), (100, 0)) * 0.8
    left_knee_percentage = np.interp(body.left_knee_angle, (174, 177), (100, 0)) * 0.2
    percentage = int(right_knee_percentage + left_knee_percentage)
    return verify_rep(percentage, direction)


def squats(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (65, 175), (100, 0)) * 0.5
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (90, 110), (0, 100)) * 0.5
    percentage = int(right_knee_percentage + right_shoulder_percentage)
    return verify_rep(percentage, direction)


def hip_stretch_left_leg(body, direction):
    right_knee_percentage = np.interp(body.right_knee_angle, (45, 90), (100, 0)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 130), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def hip_stretch_right_leg(body, direction):
    left_knee_percentage = np.interp(body.left_knee_angle, (45, 90), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 130), (0, 100)) * 0.5
    percentage = int(left_knee_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def good_morning_stretch(body, direction):
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (90, 175), (100, 0)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (150, 175), (100, 0)) * 0.5
    percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep(percentage, direction)


def press_up_back(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (160, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def left_leg_elevation(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (160, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def right_leg_elevation(body, direction):
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (160, 175), (100, 0))
    return verify_rep(int(left_outer_hip_percentage), direction)


def box_push_ups(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (75, 90), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def cobra_stretch(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (150, 175), (100, 0)) * 0.6
    right_elbow_percentage = np.interp(body.right_elbow_angle, (25, 175), (0, 100)) * 0.4
    percentage = int(right_outer_hip_percentage + right_elbow_percentage)
    return verify_rep(percentage, direction)


def crunch_kicks(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (80, 130), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (60, 175), (100, 0)) * 0.5
    percentage = int(right_outer_hip_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def leg_drops(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (90, 175), (100, 0))
    return verify_rep(int(right_outer_hip_percentage), direction)


def military_push_ups(body, direction):
    right_elbow_percentage = np.interp(body.right_elbow_angle, (90, 170), (100, 0))
    return verify_rep(int(right_elbow_percentage), direction)


def superman(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (160, 175), (100, 0)) * 0.5
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (160, 175), (100, 0)) * 0.5
    percentage = int(right_outer_hip_percentage + right_shoulder_percentage)
    return verify_rep(percentage, direction)


def donkey_kicks_pulse_left(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (165, 175), (0, 100)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (85, 95), (100, 0)) * 0.5
    percentage = int(right_outer_hip_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def donkey_kicks_pulse_right(body, direction):
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (165, 175), (0, 100)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (85, 95), (100, 0)) * 0.5
    percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep(percentage, direction)


def glute_kick_back_pulse_left(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (165, 175), (100, 0)) * 0.7
    right_knee_percentage = np.interp(body.right_knee_angle, (170, 175), (0, 100)) * 0.3
    percentage = int(right_outer_hip_percentage + right_knee_percentage)
    return verify_rep(percentage, direction)


def glute_kick_back_pulse_right(body, direction):
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (165, 175), (100, 0)) * 0.7
    left_knee_percentage = np.interp(body.left_knee_angle, (170, 175), (0, 100)) * 0.3
    percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep_double_sided_exercises(percentage, direction)


def jumping_jacks(body, direction):
    left_shoulder_percentage = np.interp(body.left_shoulder_angle, (15, 175), (0, 100)) * 0.25
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (15, 175), (0, 100)) * 0.25
    left_inner_hip_percentage = np.interp(body.left_inner_hip_angle, (90, 100), (0, 100)) * 0.25
    right_inner_hip_percentage = np.interp(body.right_inner_hip_angle, (90, 100), (0, 100)) * 0.25
    return verify_rep(int(left_inner_hip_percentage + right_inner_hip_percentage +
                          left_shoulder_percentage + right_shoulder_percentage), direction)


# double sided exercises


def side_bends(body, direction):
    # user should always start with left side
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (100, 145), (100, 0))
    left_shoulder_percentage = np.interp(body.left_shoulder_angle, (100, 145), (100, 0))
    if direction < 2:
        percentage = right_shoulder_percentage
    else:
        percentage = left_shoulder_percentage
    return verify_rep_double_sided_exercises(percentage, direction)


def donkey_kicks(body, direction):
    # user should always start with left side
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (90, 175), (0, 100)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (88, 90), (100, 0)) * 0.5
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (90, 175), (0, 100)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (88, 90), (100, 0)) * 0.5

    if direction < 2:
        percentage = int(right_outer_hip_percentage + right_knee_percentage)
    else:
        percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep_double_sided_exercises(percentage, direction)


def glute_kick_back(body, direction):
    # user should always start with left side
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (90, 160), (0, 100)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 170), (0, 100)) * 0.5
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (90, 160), (0, 100)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 170), (0, 100)) * 0.5

    if direction < 2:
        percentage = int(right_outer_hip_percentage + right_knee_percentage)
    else:
        percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep_double_sided_exercises(percentage, direction)


def bicycle_crunches(body, direction):
    # user should always start with left side
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (100, 0))
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (100, 0))
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (130, 175), (100, 0))
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (130, 175), (100, 0))

    if direction < 2:
        percentage = int(right_knee_percentage * 0.5 + right_outer_hip_percentage * 0.5)
    else:
        percentage = int(left_knee_percentage * 0.5 + left_outer_hip_percentage * 0.5)
    return verify_rep_double_sided_exercises(percentage, direction)


def bird_dog(body, direction):
    # user should always start with left side
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (0, 100))
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (0, 100))
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (90, 175), (0, 100))
    left_shoulder_percentage = np.interp(body.left_shoulder_angle, (90, 175), (0, 100))

    if direction < 2:
        percentage = int(right_knee_percentage * 0.5 + left_shoulder_percentage * 0.5)
    else:
        percentage = int(left_knee_percentage * 0.5 + right_shoulder_percentage * 0.5)
    return verify_rep_double_sided_exercises(percentage, direction)


def dead_bug(body, direction):
    # user should always start with left side
    right_knee_percentage = np.interp(body.right_knee_angle, (90, 175), (0, 100))
    left_knee_percentage = np.interp(body.left_knee_angle, (90, 175), (0, 100))
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (90, 175), (0, 100))
    left_shoulder_percentage = np.interp(body.left_shoulder_angle, (90, 175), (0, 100))

    if direction < 2:
        percentage = int(right_knee_percentage * 0.5 + left_shoulder_percentage * 0.5)
    else:
        percentage = int(left_knee_percentage * 0.5 + right_shoulder_percentage * 0.5)
    return verify_rep_double_sided_exercises(percentage, direction)


def diagonal_plank(body, direction):
    # user should always start with left side: unghi genunchi
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (140, 175), (0, 100))
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (140, 175), (0, 100))
    right_shoulder_percentage = np.interp(body.right_shoulder_angle, (80, 140), (0, 100))
    left_shoulder_percentage = np.interp(body.left_shoulder_angle, (80, 175), (0, 100))

    if direction < 2:
        percentage = int(right_outer_hip_percentage * 0.5 + left_shoulder_percentage * 0.5)
    else:
        percentage = int(left_outer_hip_percentage * 0.5 + right_shoulder_percentage * 0.5)
    return verify_rep_double_sided_exercises(percentage, direction)


def leg_raise(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (90, 175), (100, 0))
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (90, 175), (100, 0))
    if direction < 2:
        percentage = int(right_outer_hip_percentage)
    else:
        percentage = int(left_outer_hip_percentage)
    return verify_rep_double_sided_exercises(percentage, direction)


def flutter_kicks(body, direction):
    right_outer_hip_percentage = np.interp(body.right_outer_hip_angle, (130, 160), (100, 0)) * 0.5
    right_knee_percentage = np.interp(body.right_knee_angle, (170, 175), (0, 100)) * 0.5
    left_outer_hip_percentage = np.interp(body.left_outer_hip_angle, (130, 160), (100, 0)) * 0.5
    left_knee_percentage = np.interp(body.left_knee_angle, (170, 175), (0, 100)) * 0.5
    if direction < 2:
        percentage = int(right_outer_hip_percentage + right_knee_percentage)
    else:
        percentage = int(left_outer_hip_percentage + left_knee_percentage)
    return verify_rep_double_sided_exercises(percentage, direction)
