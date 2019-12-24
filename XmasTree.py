#!/usr/bin/env python3

"""This tree blinks randomly."""

import os
import sys
import threading
import random
from time import sleep

reds = []
blues = []
greens = []
yellows = []
tree = list(open('tree.txt').read().rstrip())
frametime = 1/15
quiting = False


def printTree():
    """Print the tree to the terminal."""
    out = "".join(tree)
    sleep(frametime/2)
    os.system('clear')
    print(out)
    sleep(frametime/2)


def exit():
    """Exit nicely cleaning up."""
    os.system('setterm -cursor on')
    global quiting
    quiting = True
    for t in [tr, ty, tb, tg]:
        t.join()
    sys.exit(1)


def blink(color, lights):
    """Blink an individual light."""
    while True:
        global quiting
        if quiting:
            break
        for light in lights:
            if random.randint(0, 10) <= 9:
                if color == "red":
                    tree[light] = f"\033[91m•\033[0m"
                if color == "green":
                    tree[light] = f"\033[92m•\033[0m"
                if color == "yellow":
                    tree[light] = f"\033[93m&\033[0m"
                if color == "blue":
                    tree[light] = f"\033[94m•\033[0m"
            else:
                tree[light] = "•"
        sleep(frametime*2)


for i, x in enumerate(tree):
    if x == '*':
        blues.append(i)
    if x == '@':
        reds.append(i)
    if x == '%':
        greens.append(i)
    if x == '2':
        yellows.append(i)

tr = threading.Thread(target=blink, args=('red', reds))
tb = threading.Thread(target=blink, args=('blue', blues))
tg = threading.Thread(target=blink, args=('green', greens))
ty = threading.Thread(target=blink, args=('yellow', yellows))
os.system('setterm -cursor off')
for t in [tr, tb, tg, ty]:
    t.start()
try:
    while True:
        printTree()
except KeyboardInterrupt:
    exit()
finally:
    exit()

sys.exit(0)
