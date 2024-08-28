import numpy as np
import cv2 as cv
import mediapipe as mp
import pygame

from sprite import AnimatedSprite

mp_pose = mp.solutions.pose


# Function to calculate the angle between three joints
class Utils:
    width = 1280
    height = 1024
    fps = 30
    font = '../resources/fonts/Laro Soft Medium.ttf'
    ORANGE_SHADE_DARK = (215, 74, 20)
    ORANGE_SHADE_BRIGHT = (255, 134, 80)
    GRAY_SHADE = (64, 61, 57)
    WHITE_SHADE = (255, 252, 242)
    BLACK = (0, 0, 0)

    landmark_dict = {
        'nose': mp_pose.PoseLandmark.NOSE,
        'left_eye_inner': mp_pose.PoseLandmark.LEFT_EYE_INNER,
        'left_eye': mp_pose.PoseLandmark.LEFT_EYE,
        'left_eye_outer': mp_pose.PoseLandmark.LEFT_EYE_OUTER,
        'right_eye_inner': mp_pose.PoseLandmark.RIGHT_EYE_INNER,
        'right_eye': mp_pose.PoseLandmark.RIGHT_EYE,
        'right_eye_outer': mp_pose.PoseLandmark.RIGHT_EYE_OUTER,
        'left_ear': mp_pose.PoseLandmark.LEFT_EAR,
        'right_ear': mp_pose.PoseLandmark.RIGHT_EAR,
        'mouth_left': mp_pose.PoseLandmark.MOUTH_LEFT,
        'mouth_right': mp_pose.PoseLandmark.MOUTH_RIGHT,
        'left_shoulder': mp_pose.PoseLandmark.LEFT_SHOULDER,
        'right_shoulder': mp_pose.PoseLandmark.RIGHT_SHOULDER,
        'left_elbow': mp_pose.PoseLandmark.LEFT_ELBOW,
        'right_elbow': mp_pose.PoseLandmark.RIGHT_ELBOW,
        'left_wrist': mp_pose.PoseLandmark.LEFT_WRIST,
        'right_wrist': mp_pose.PoseLandmark.RIGHT_WRIST,
        'left_pinky': mp_pose.PoseLandmark.LEFT_PINKY,
        'right_pinky': mp_pose.PoseLandmark.RIGHT_PINKY,
        'left_index': mp_pose.PoseLandmark.LEFT_INDEX,
        'right_index': mp_pose.PoseLandmark.RIGHT_INDEX,
        'left_thumb': mp_pose.PoseLandmark.LEFT_THUMB,
        'right_thumb': mp_pose.PoseLandmark.RIGHT_THUMB,
        'left_hip': mp_pose.PoseLandmark.LEFT_HIP,
        'right_hip': mp_pose.PoseLandmark.RIGHT_HIP,
        'left_knee': mp_pose.PoseLandmark.LEFT_KNEE,
        'right_knee': mp_pose.PoseLandmark.RIGHT_KNEE,
        'left_ankle': mp_pose.PoseLandmark.LEFT_ANKLE,
        'right_ankle': mp_pose.PoseLandmark.RIGHT_ANKLE,
        'left_heel': mp_pose.PoseLandmark.LEFT_HEEL,
        'right_heel': mp_pose.PoseLandmark.RIGHT_HEEL,
        'left_foot_index': mp_pose.PoseLandmark.LEFT_FOOT_INDEX,
        'right_foot_index': mp_pose.PoseLandmark.RIGHT_FOOT_INDEX
    }

    @staticmethod
    def process_image(image, pose):
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        cv.cvtColor(image, cv.COLOR_RGB2BGR)
        return results

    @staticmethod
    def display_angles(frame, body):
        if body is None:
            print("No body detected")
            return
        angles = [
            # (body.left_elbow_angle, body.left_elbow),
            # (body.right_elbow_angle, body.right_elbow),
            # (body.left_shoulder_angle, body.left_shoulder),
            # (body.right_shoulder_angle, body.right_shoulder),
            # (body.left_knee_angle, body.left_knee),
            # (body.right_knee_angle, body.right_knee),
            # (body.left_outer_hip_angle, body.lesft_hip),
            # (body.left_inner_hip_angle, body.left_hip),
            # (body.right_outer_hip_angle, body.right_hip),
            # (body.right_inner_hip_angle, body.right_hip)
        ]

        for angle, part in angles:
            Utils.put_text_on_frame(frame, angle, part)

    @staticmethod
    def put_text_on_frame(frame, body_angle, body_part):
        w, h, _ = frame.shape
        cv.putText(frame, str(body_angle),
                   tuple(np.multiply(body_part, [w, h]).astype(int)),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv.LINE_AA
                   )

    @staticmethod
    def get_gif_from_url(image_url, scale):
        animation_frame_list = AnimatedSprite.loadGIF(image_url, scale)
        animated_sprite = AnimatedSprite(200, Utils.height - 50, animation_frame_list)
        gif = pygame.sprite.Group(animated_sprite)
        return gif
