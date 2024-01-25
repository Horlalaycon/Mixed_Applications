# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

import pyautogui
import string
import random


screenshot_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
screenshot_name += ".png"

# specify the path to save the screenshot e.g C:/Temp/
screenshot_path = "C:/Temp/"
pyautogui.screenshot(screenshot_path + screenshot_name)
print(f"Screenshot has been taken, file saved to {screenshot_path + screenshot_name}")
