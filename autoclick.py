#!/usr/bin/python3 
from time import sleep
import pyautogui
import sys

click_per_sec = 30
MIN = (2900, 620)
MAX = (2950, 660)


# mouse_pos = pyautogui.position()
# # sleep(1)
# # while mouse_pos != pyautogui.position():
# #     mouse_pos = pyautogui.position();
# #     sleep(.25)

mouse_pos = pyautogui.position()

if len(sys.argv) > 1:
    click_count = int(sys.argv[1])
if len(sys.argv) == 3:
    click_per_sec = float(sys.argv[2])

clicks_left = click_count
click_delay = 1 / click_per_sec
pyautogui.PAUSE = click_delay

try:
    while clicks_left > 0:
        cur_x,cur_y = pyautogui.position()
        print(F"\rClicks Left:{clicks_left:10d} \t\tPoint({cur_x:4d},{cur_y:4d})\033[K", end="", flush=True)
        if (cur_x < MIN[0] or cur_x > MAX[0]
            or cur_y < MIN[1] or cur_y > MAX[1]):
            sleep(.1)
            # clicks_left = 0
            continue
        clicks_left = clicks_left - 1
        pyautogui.click()
    else:
        print("Done")

except KeyboardInterrupt:
    print("\033[D\033[D\033[K\nCtrl-c Exiting")