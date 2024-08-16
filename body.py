from dataclasses import dataclass
from typing import ClassVar
import numpy as np


@dataclass
class Body:
    nose: np.array
    left_eye_inner: np.array
    left_eye: np.array
    left_eye_outer: np.array
    right_eye_inner: np.array
    right_eye: np.array
    right_eye_outer: np.array
    left_ear: np.array
    right_ear: np.array
    mouth_left: np.array
    mouth_right: np.array
    left_shoulder: np.array
    right_shoulder: np.array
    left_elbow: np.array
    right_elbow: np.array
    left_wrist: np.array
    right_wrist: np.array
    left_pinky: np.array
    right_pinky: np.array
    left_index: np.array
    right_index: np.array
    left_thumb: np.array
    right_thumb: np.array
    left_hip: np.array
    right_hip: np.array
    left_knee: np.array
    right_knee: np.array
    left_ankle: np.array
    right_ankle: np.array
    left_heel: np.array
    right_heel: np.array
    left_foot_index: np.array
    right_foot_index: np.array
    left_elbow_angle: ClassVar[float]
    right_elbow_angle: ClassVar[float]
    left_shoulder_angle: ClassVar[float]
    right_shoulder_angle: ClassVar[float]
    left_knee_angle: ClassVar[float]
    right_knee_angle: ClassVar[float]
    left_outer_hip_angle: ClassVar[float]
    left_inner_hip_angle: ClassVar[float]
    right_outer_hip_angle: ClassVar[float]
    right_inner_hip_angle: ClassVar[float]
    torso_tilt: ClassVar[float]

    @property
    def left_elbow_angle(self) -> float:
        return Body.calculate_angle(self.left_shoulder, self.left_elbow, self.left_wrist)

    @property
    def right_elbow_angle(self) -> float:
        return Body.calculate_angle(self.right_shoulder, self.right_elbow, self.right_wrist)

    @property
    def left_shoulder_angle(self) -> float:
        return Body.calculate_angle(self.left_hip, self.left_shoulder, self.left_elbow)

    @property
    def right_shoulder_angle(self) -> float:
        return Body.calculate_angle(self.right_hip, self.right_shoulder, self.right_elbow)

    @property
    def left_knee_angle(self) -> float:
        return Body.calculate_angle(self.left_hip, self.left_knee, self.left_ankle)

    @property
    def right_knee_angle(self) -> float:
        return Body.calculate_angle(self.right_hip, self.right_knee, self.right_ankle)

    @property
    def left_outer_hip_angle(self) -> float:
        return Body.calculate_angle(self.left_shoulder, self.left_hip, self.left_knee)

    @property
    def left_inner_hip_angle(self) -> float:
        return Body.calculate_angle(self.left_knee, self.left_hip, self.right_hip)

    @property
    def right_outer_hip_angle(self) -> float:
        return Body.calculate_angle(self.right_shoulder, self.right_hip, self.right_knee)

    @property
    def right_inner_hip_angle(self) -> float:
        return Body.calculate_angle(self.right_knee, self.right_hip, self.left_hip)

    #TODO: Implement torso tilt

    @staticmethod
    def calculate_angle(a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle
