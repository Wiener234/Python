import pyautogui
from time import sleep
import keyboard
import win32api, win32con

while keyboard.is_pressed("Esc") == False:
    if pyautogui.locateOnScreen('image.png', confidence=0.7):
        print("I see it")
        sleep(0.5)
    else:
        print("I cant see it")
        sleep(0.5)