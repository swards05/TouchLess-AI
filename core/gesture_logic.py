# File path: core/gesture_logic.py
# Expected output:
# - Detects finger patterns from HandTracker
# - Returns gesture names like VOLUME, BRIGHTNESS, MOUSE, SCREENSHOT, CALCULATOR, CLOSE
# File path: core/gesture_logic.py
import math


class GestureLogic:
    def calculate_distance(self, p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    def map_distance_to_percent(self, distance, min_dist=20, max_dist=250):
        distance = max(min_dist, min(max_dist, distance))
        return int(((distance - min_dist) / (max_dist - min_dist)) * 100)