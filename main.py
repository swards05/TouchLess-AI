# File path: main.py
# Expected output:
# - Opens webcam
# - Tracks fingers in real time
# - Detects gesture names
# - Performs system actions live
import cv2
import time
from core.hand_tracker import HandTracker
from core.gesture_logic import GestureLogic
from core.system_control import SystemControl
from core.mouse_control import MouseControl
from core.smoothing import Smoother
from core.config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    logic = GestureLogic()
    control = SystemControl()
    mouse = MouseControl()
    smoother = Smoother()

    last_gesture = "NONE"
    cooldown_time = 1
    last_action_time = time.time()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame, landmarks = tracker.find_hands(frame)

        gesture = "NONE"

        if landmarks:
            fingers = tracker.fingers_up()
            gesture = logic.detect_gesture(fingers)

            current_time = time.time()

            # ===== DYNAMIC VOLUME =====
            if gesture == "VOLUME" and len(landmarks) > 8:
                thumb = (landmarks[4][1], landmarks[4][2])
                index = (landmarks[8][1], landmarks[8][2])

                dist = logic.calculate_distance(thumb, index)
                volume_percent = logic.map_distance_to_percent(dist)

                if volume_percent > 70:
                    control.volume_up()
                elif volume_percent < 30:
                    control.volume_down()

                cv2.putText(frame, f"Volume: {volume_percent}%", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # ===== DYNAMIC BRIGHTNESS =====
            elif gesture == "BRIGHTNESS" and len(landmarks) > 12:
                thumb = (landmarks[4][1], landmarks[4][2])
                middle = (landmarks[12][1], landmarks[12][2])

                dist = logic.calculate_distance(thumb, middle)
                brightness_percent = logic.map_distance_to_percent(dist)

                control.set_brightness(brightness_percent)

                cv2.putText(frame, f"Brightness: {brightness_percent}%", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # ===== OTHER GESTURES =====
            elif gesture != last_gesture and (current_time - last_action_time) > cooldown_time:
                if gesture == "CALCULATOR":
                    control.open_calculator()

                elif gesture == "SCREENSHOT":
                    filename = control.take_screenshot()
                    print(f"Saved: {filename}")

                elif gesture == "CLOSE":
                    control.close_window()

                last_action_time = current_time
                last_gesture = gesture

            # ===== MOUSE MOVE + CLICK =====
            if gesture == "MOUSE" and len(landmarks) > 8:
                x, y = landmarks[8][1], landmarks[8][2]
                sx, sy = smoother.smooth(x, y)
                mouse.move(sx, sy, SCREEN_WIDTH, SCREEN_HEIGHT, frame.shape[1], frame.shape[0])

                # pinch click
                thumb = (landmarks[4][1], landmarks[4][2])
                index = (landmarks[8][1], landmarks[8][2])
                click_distance = logic.calculate_distance(thumb, index)

                if click_distance < 30:
                    mouse.click()
                    time.sleep(0.3)

            # ===== SCROLL =====
            elif fingers == [0, 1, 1, 0, 0] and len(landmarks) > 12:
                index_y = landmarks[8][2]
                middle_y = landmarks[12][2]

                if index_y < middle_y:
                    mouse.scroll_up()
                else:
                    mouse.scroll_down()

                time.sleep(0.2)

        cv2.putText(frame, f"Gesture: {gesture}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("TouchLess AI", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()