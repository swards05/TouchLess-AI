# File path: main.py
# Expected output:
# - Opens webcam
# - Tracks fingers in real time
# - Detects gesture names
# - Performs system actions live
# File path: main.py
# File path: main.py

import cv2
import time
from core.hand_tracker import HandTracker
from core.gesture_logic import GestureLogic
from core.system_control import SystemControl
from core.mouse_control import MouseControl
from core.calibration import calibrate_ranges


def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    logic = GestureLogic()
    control = SystemControl()
    mouse = MouseControl()
    volume_min, volume_max, brightness_min, brightness_max = calibrate_ranges(
    cap, tracker, logic )

    cooldown_time = 1
    last_action_time = time.time()
    prev_scroll_y = None

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame, landmarks = tracker.find_hands(frame)

        gesture = "NONE"

        if landmarks and len(landmarks) >= 21:
            fingers = tracker.fingers_up()

            thumb = (landmarks[4][1], landmarks[4][2])
            index = (landmarks[8][1], landmarks[8][2])
            middle = (landmarks[12][1], landmarks[12][2])
            pinky = (landmarks[20][1], landmarks[20][2])

            thumb_index_dist = logic.calculate_distance(thumb, index)
            thumb_pinky_dist = logic.calculate_distance(thumb, pinky)

            # ================= SCREENSHOT =================
            if fingers == [1, 0, 0, 0, 0]:
                current_time = time.time()
                if current_time - last_action_time > cooldown_time:
                    filename = control.take_screenshot()
                    print(f"Saved: {filename}")
                    last_action_time = current_time
                gesture = "SCREENSHOT"

            # ================= SCROLL =================
            elif fingers == [0, 1, 1, 0, 0]:
                # move hand vertically for direction
                # ================= SCROLL =================
                current_scroll_y = index[1]

                if prev_scroll_y is not None:
                    diff = prev_scroll_y - current_scroll_y

                    if diff > 15:
                        mouse.scroll_up()
                    elif diff < -15:
                        mouse.scroll_down()

                prev_scroll_y = current_scroll_y
                gesture = "SCROLL"
                time.sleep(0.1)

            # ================= VOLUME =================
            elif fingers== [1,1,0,0,0]:
                volume_percent = logic.map_distance_to_percent(
                    thumb_index_dist,
                    min_dist=volume_min,
                    max_dist=volume_max
                )

                if volume_percent >= 65:
                    control.volume_up()
                elif volume_percent <= 35:
                    control.volume_down()

                gesture = "VOLUME"

                cv2.putText(frame, f"Volume: {volume_percent}%", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.line(frame, thumb, index, (255, 0, 255), 3)

            # ================= BRIGHTNESS =================
            elif fingers==[1,0,0,0,1]:
                safe_min = min(brightness_min, 80)
                safe_max = max(brightness_max, 260)

                brightness_percent = logic.map_distance_to_percent(
                    thumb_pinky_dist,
                    min_dist=safe_min,
                    max_dist=safe_max
                )

                control.set_brightness(brightness_percent)
                gesture = "BRIGHTNESS"

                cv2.putText(frame, f"Brightness: {brightness_percent}%", (20, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                cv2.line(frame, thumb, pinky, (0, 255, 255), 3)

        cv2.putText(frame, f"Gesture: {gesture}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("TouchLess AI", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()