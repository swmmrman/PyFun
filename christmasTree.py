#!/usr/bin/env python3

"""Christmas scene for shits and giggle."""
import os
import sys
from time import sleep

stime = .25
colors = ["red", "green", "blue"]
state = 0
os.system('setterm -cursor off')
scene = open('tree.txt').readlines()
dtime = (1/60) if len(sys.argv) > 1 and sys.argv[1] == "-s" else 0
try:
    while True:
        sceneTemp = open('tree.txt').readlines()  # scene
        os.system('clear')
        for line in sceneTemp:
            line = line.replace("2", "\033[1;33;40m&\033[1;37;40m")
            if state > 0:
                line = line.replace("*", "\033[1;34;40m*\033[1;37;40m")
                line = line.replace("@", "\033[1;32;40m*\033[1;37;40m")
                line = line.replace("%", "\033[1;31;40m*\033[1;37;40m")
            else:
                line = line.replace("*", " ")
                line = line.replace("@", " ")
                line = line.replace("%", " ")
            print(f"{line}", end='')
            sleep(dtime)
        print("")
        state = (state + 1) % 2
        sleep(stime)
except KeyboardInterrupt:
    sleep(.1)
finally:
    os.system('setterm -cursor on')
    sys.exit(0)
