# File path: core/system_control.py
# Expected output:
# - Controls system volume
# - Controls screen brightness
# - Takes screenshots
# - Opens calculator
# - Closes active window
import os
import pyautogui
import screen_brightness_control as sbc
from datetime import datetime
    

class SystemControl:
    def take_screenshot(self):
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        return filename

    def open_calculator(self):
        os.system("start calc")

    def close_window(self):
        pyautogui.hotkey("alt", "f4")

    def set_brightness(self, value):
        value = max(0, min(100, int(value)))
        sbc.set_brightness(value)

    def volume_up(self):
        pyautogui.press("volumeup")

    def volume_down(self):
        pyautogui.press("volumedown")