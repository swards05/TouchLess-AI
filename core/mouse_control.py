# File path: core/mouse_control.py
# Expected output:
# - Saves screenshot with timestamped filename

import pyautogui


class MouseControl:
    def move(self, x, y, screen_w, screen_h, frame_w, frame_h):
        mouse_x = max(0, min(screen_w, int((x / frame_w) * screen_w)))
        mouse_y = max(0, min(screen_h, int((y / frame_h) * screen_h)))
        pyautogui.moveTo(mouse_x, mouse_y, duration=0.01)

    def click(self):
        pyautogui.click()

    def scroll_up(self):
        pyautogui.scroll(300)

    def scroll_down(self):
        pyautogui.scroll(-300)