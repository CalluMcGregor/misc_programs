import time
import pyautogui

#TODO add a noise when time is up

def click_mouse():
    """function that clicks mouse every 60 seconds for user defined minutes"""
    minutes_passed = 0
    time_limit = input("Enter the number of minutes you want your computer to stay active: ")
    time_limit = int(time_limit)
    print("Starting")
    while minutes_passed < time_limit:
        pyautogui.press('f13')
        time.sleep(60)
        minutes_passed += 1
        print(minutes_passed)

click_mouse()