# File path: core/gesture_logic.py
# Expected output:
# - Detects finger patterns from HandTracker
# - Returns gesture names like VOLUME, BRIGHTNESS, MOUSE, SCREENSHOT, CALCULATOR, CLOSE
import math


class GestureLogic:
    def detect_gesture(self, fingers):
        if fingers == [1, 0, 0, 0, 0]:
            return "CALCULATOR"

        elif fingers == [0, 1, 0, 0, 0]:
            return "MOUSE"

        elif fingers == [0, 1, 1, 1, 0]:
            return "SCREENSHOT"

        elif fingers == [0, 0, 0, 0, 0]:
            return "CLOSE"

        elif fingers == [1, 1, 0, 0, 0]:
            return "VOLUME"

        elif fingers == [1, 0, 1, 0, 0]:
            return "BRIGHTNESS"

        return "NONE"

    def calculate_distance(self, p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    def map_distance_to_percent(self, distance, min_dist=20, max_dist=200):
        distance = max(min_dist, min(max_dist, distance))
        return int(((distance - min_dist) / (max_dist - min_dist)) * 100)