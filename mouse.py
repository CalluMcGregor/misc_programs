import time
import pyautogui

def click_mouse():
    """function that clicks mouse every 60 seconds for user defined minutes"""
    minutes_passed = 0
    time_limit = input("Enter the number of minutes you want your computer to stay active: ")
    time_limit = int(time_limit)
    while minutes_passed < time_limit:
        pyautogui.click(None, None)
        time.sleep(60)
        minutes_passed += 1
        print(minutes_passed)

click_mouse()