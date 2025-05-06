import simplecontroller as sc
import time 

device = sc.Board("COM7")
device.pinMode(2, sc.OUTPUT)
#device.pinMode(13, sc.INPUT_PULLUP)

while True:
    device.digitalWrite(2, True)
    time.sleep(1)
    device.digitalWrite(2, False)
    time.sleep(1)
    #device.digitalWrite(2, not device.digitalRead(13))
    