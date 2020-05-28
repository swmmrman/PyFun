#!/usr/bin/env python3
import psutil
import os
import sys
import time

pid = os.getpid()
pidFile = '/tmp/pidTests.pid'
if os.path.exists(pidFile):
    f = open(pidFile, "r")
    oldPid = int(f.readline())
    f.close()
else:
    oldPid = False

if oldPid and psutil.pid_exists(oldPid):
    print("Other instance running.")
    sys.exit(1)
elif oldPid:
    os.remove(pidFile)

f = open(pidFile, 'w')
f.write(str(pid))
f.close()
try:
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    os.remove(pidFile)
