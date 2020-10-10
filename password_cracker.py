from time import sleep
from datetime import datetime
import pyautogui, keyboard, win32api, win32con

sleep(5)

file = open("password.txt", "r")

x = 188
y = 230



for word in file:
    timestart = datetime.now().strftime("%H:%M:%S")
    print(timestart)
    pyautogui.typewrite(word)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(0.5)
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.press("delete")
    timeend = datetime.now().strftime("%H:%M:%S")
    print(timeend)
    if pyautogui.locateOnScreen('test.png', confidence=0.9):
        break

    if keyboard.is_pressed("Esc"):
        break

