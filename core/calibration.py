# File path: core/calibration.py
# Expected output:
# - Guides user to calibrate volume + brightness ranges
# - Returns personalized min/max distances
# File path: core/calibration.py
# File path: core/calibration.py

import cv2
import time


def calibrate_ranges(cap, tracker, logic):
    steps = [
        ("Thumb + Index CLOSE", "min", 8),
        ("Thumb + Index FAR", "max", 8),
        ("Thumb + Pinky CLOSE", "min", 20),
        ("Thumb + Pinky FAR", "max", 20),
    ]

    captured = []

    for step_text, mode, point_id in steps:
        distances = []
        start = time.time()

        while True:
            success, frame = cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            frame, landmarks = tracker.find_hands(frame)

            cv2.putText(
                frame,
                f"Calibration: {step_text}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            cv2.imshow("TouchLess AI", frame)

            if landmarks and len(landmarks) >= 21:
                thumb = (landmarks[4][1], landmarks[4][2])
                other = (landmarks[point_id][1], landmarks[point_id][2])

                dist = logic.calculate_distance(thumb, other)
                distances.append(dist)

            if cv2.waitKey(1) & 0xFF == 27:
                break

            if time.time() - start > 2:
                break

        # ✅ safe fallback if no distances captured
        if not distances:
            if point_id == 8:
                distances = [50, 250]
            else:
                distances = [80, 500]

        if mode == "min":
            captured.append(min(distances))
        else:
            captured.append(max(distances))

    # ✅ guaranteed 4 values
    while len(captured) < 4:
        captured.append(300)

    volume_min, volume_max, brightness_min, brightness_max = captured[:4]

    # extra safety
    if volume_max <= volume_min:
        volume_max = volume_min + 150

    if brightness_max <= brightness_min:
        brightness_max = brightness_min + 250

    print("Calibration Complete:")
    print("Volume:", volume_min, volume_max)
    print("Brightness:", brightness_min, brightness_max)

    return volume_min, volume_max, brightness_min, brightness_max