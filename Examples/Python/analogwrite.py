import simplecontroller as sc
import time

device = sc.Board("/dev/cu.usbserial-0001")

while True:
    device.analogWrite(2, device.analogRead(13))
    time.sleep(0.1)