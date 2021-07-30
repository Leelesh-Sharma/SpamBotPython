import pyautogui
import time
time.sleep(5)
f = ('context','r')
while True:
    pyautogui.typewrite(f)
    pyautogui.press("enter")
