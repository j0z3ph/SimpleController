import simplecontroller as sc

device = sc.Board("/dev/cu.usbserial-0001")
device.pinMode(13, sc.INPUT_PULLUP)

while True:
    print(device.digitalRead(13))