import serial
from datetime import datetime
ser = serial.Serial('/dev/ttyUSB0', 115200)
log = open('tempNano.log', 'w')


try:
  while True:
    now = datetime.now()
    line = ser.readline().decode().strip("\r\n")
    print(line)
    log.write(F"[{now.ctime()}] {line}\n")
    log.flush()
except KeyboardInterrupt:
  print("\nBye Now")
finally:
  ser.close()
