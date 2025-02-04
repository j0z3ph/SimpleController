import sscontroller
import time

device = sscontroller.Board("/dev/cu.usbmodem1101")
device.attachServo(9)
#device.pinMode(2, sscontroller.OUTPUT)
angle = 0
while True:
    device.servoWrite(angle)
    angle += 10
    if angle > 180:
        angle = 0
    time.sleep(1)
    #device.digitalWrite(2, True)
    #time.sleep(1)
    #device.digitalWrite(2, False)
    #time.sleep(1)
    #device.analogWrite(2, device.analogRead(13))
    #print(device.analogRead(13))
    #time.sleep(0.1)