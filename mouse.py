import time
import pyautogui
import sys

#TODO add a noise when time is up

def click_mouse():
    """function that clicks mouse every 60 seconds for user defined minutes"""
    minutes_passed = 0
    if len(sys.argv) > 1:
        active_duration = int(sys.argv[1])
    else:
        active_duration = int(input("Enter an integer for the number of minutes: "))

    print(f"Keeping your laptop active for: {active_duration} minutes.")
    while minutes_passed < active_duration:
        pyautogui.press('f13')
        time.sleep(60)
        minutes_passed += 1
        print(minutes_passed)

click_mouse()