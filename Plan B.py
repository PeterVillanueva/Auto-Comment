import pyautogui
import time

comment = "https://fb.watch/iTaiZYSLBN/"

time.sleep(5)

for i in range(1000):
    pyautogui.typewrite(comment)
    pyautogui.typewrite("\n")
    time.sleep(1)