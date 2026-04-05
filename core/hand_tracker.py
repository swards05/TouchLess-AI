#file path: core/hand_tracker.py

import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self, mode=False, max_hands=1, detection_conf=0.85, track_conf=0.85):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.track_conf = track_conf

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_conf,
            min_tracking_confidence=self.track_conf
        )

        self.mp_draw = mp.solutions.drawing_utils
        self.landmarks = []

    def find_hands(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        self.landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

                h, w, _ = frame.shape
                for idx, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.landmarks.append((idx, cx, cy))

        return frame, self.landmarks

    def fingers_up(self):
        fingers = [0, 0, 0, 0, 0]

        if not self.landmarks:
            return fingers

        tip_ids = [4, 8, 12, 16, 20]

        # Thumb
        if self.landmarks[4][1] > self.landmarks[3][1]:
            fingers[0] = 1

        # Other fingers
        for i in range(1, 5):
            if self.landmarks[tip_ids[i]][2] < self.landmarks[tip_ids[i] - 2][2]:
                fingers[i] = 1

        return fingers