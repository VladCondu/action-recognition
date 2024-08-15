import cv2
import mediapipe as mp
import numpy as np

from utils import Utils
from body import Body

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def start_webcam_capture():
    capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    capture.set(cv2.CAP_PROP_FPS, 30)
    return capture


def build_body(frame, pose):
    frame = cv2.flip(frame, 1)
    results = Utils.process_image(frame, pose)
    landmarks = results.pose_landmarks.landmark

    body = Body(**{name: np.array([landmarks[landmark.value].x, landmarks[landmark.value].y])
                   for name, landmark in Utils.landmark_dict.items()})

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    return frame, body


def main():
    cap = start_webcam_capture()
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        try:
            while cap.isOpened():
                success, frame = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue

                frame, body = build_body(frame, pose)

                # Uncomment to display angles
                # Utils.display_angles(frame, body)

                cv2.imshow('MediaPipe Pose', frame)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
