import time
import pyautogui
import cv2
import numpy as np

# loading a screenshot of the "Acknowledge" button
acknowledge_template = cv2.imread('acknowledge_button.png', cv2.IMREAD_GRAYSCALE)

while True:
    # screenshots
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot) # make the screenshot a numpy array
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) # convert to grayscale

    # Match template
    result = cv2.matchTemplate(screenshot_gray, acknowledge_template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # if match is strong enough then click the button 
    if max_val > 0.8:
        button_x, button_y = max_loc
        pyautogui.moveTo(button_x + 10, button_y + 10)  # TODO: check if need to adjust the offset
        pyautogui.click()
        print("Acknowledge button clicked!")

    time.sleep(300)  # Wait 5 min before scanning again
