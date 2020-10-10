import time, pyautogui, keyboard

time.sleep(5)

f = open("beemove", "r")


for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if keyboard.is_pressed("Esc"):
        break






