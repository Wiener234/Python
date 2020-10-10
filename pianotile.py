from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  592 Y:  600 RGB: ( 86,  88, 117)
#X:  680 Y:  600 RGB: ( 83,  85, 117)
#X:  771 Y:  600 RGB: ( 81,  84, 116)
#X:  876 Y:  600 RGB: ( 82,  85, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('Esc') == False:

    if pyautogui.pixel(592, 600)[0] == 0:
        click(592, 600)
    if pyautogui.pixel(680, 600)[0] == 0:
        click(680, 600)
    if pyautogui.pixel(771, 600)[0] == 0:
        click(771, 600)
    if pyautogui.pixel(876, 600)[0] == 0:
        click(876, 600)
