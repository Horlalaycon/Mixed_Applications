# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used take screenshots, generate random name and save it in a particular place by specifying the full path.
"""

import pyautogui
import string
import random


def take_screenshot():
    # generate random name for the screenshot
    screenshot_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

    # file extension
    screenshot_name += ".png"

    # specify the path to save the screenshot e.g C:/Temp/
    screenshot_path = "C:/Temp/"

    pyautogui.screenshot(screenshot_path + screenshot_name)
    print(f"Screenshot has been taken, file saved to {screenshot_path + screenshot_name}")


if __name__ == "__main__":
    take_screenshot()
