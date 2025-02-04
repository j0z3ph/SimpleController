import simplecontroller as sc

device = sc.Board("/dev/cu.usbserial-0001")
device.pinMode(2, sc.OUTPUT)
device.pinMode(13, sc.INPUT_PULLUP)

while True:
    device.digitalWrite(2, not device.digitalRead(13))
    