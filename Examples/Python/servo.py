import simplecontroller as sc
import time

device = sc.Board("/dev/cu.usbserial-0001")
device.attachServo(9)
angle = 0

while True:
    device.servoWrite(angle)
    angle += 10
    if angle > 180:
        angle = 0
    time.sleep(1)
    