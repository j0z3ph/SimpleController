import serial
import time

DIGITAL_READ = 0x80
DIGITAL_WRITE = 0x81
ANALOG_READ = 0x82
ANALOG_WRITE = 0x83
SERVO_WRITE = 0x84
SERVO_CONFIG = 0x85
SET_PIN_MODE = 0x86 
RESET_MESSAGE = 0xFF
DEVICE_INFO = 0xF0

INPUT = 0
OUTPUT = 1
ANALOG = 2
PWM = 3
SERVO = 4
INPUT_PULLUP = 5

ARDUINO = 0
ESP32 = 1

class Board:
    def __init__(self, port: str, baudrate: int = 115200):
        self.__serialport = serial.Serial(port, baudrate, rtscts= False, dsrdtr=False)
        self.__serialport.write(bytearray([RESET_MESSAGE,0,0,0])) # Reset
        time.sleep(2)
        self.__serialport.write(bytearray([DEVICE_INFO,0,0,0])) 
        while ord(self.__serialport.read()) != DEVICE_INFO:
            # Delete all garbage or ESP32 bootloader
            pass
        self.__device = ord(self.__serialport.read())
        #print(self.__device)
        
    def pinMode(self, pin: int, mode):
        self.__serialport.write(bytearray([SET_PIN_MODE,pin,0,mode]))     
    def digitalWrite(self, pin: int, value: bool):
        self.__serialport.write(bytearray([DIGITAL_WRITE,pin,0,value]))
    def analogWrite(self, pin: int, value: float):
        if value > 1.0:
            value = 1.0
        data = int(value * 255)
        self.__serialport.write(bytearray([ANALOG_WRITE,pin,data >> 8,data & 0x00FF]))
    def digitalRead(self, pin: int) -> bool:
        self.__serialport.write(bytearray([DIGITAL_READ,pin,0,0]))
        byte = self.__serialport.read()
        if not byte:
            return False
        data = ord(byte)
        if data == DIGITAL_READ:
            data = ord(self.__serialport.read())
            if data == pin:
                return int((self.__serialport.read() << 8) + self.__serialport.read())
        return False
    def analogRead(self, pin: int) -> float:
        self.__serialport.write(bytearray([ANALOG_READ,pin,0,0]))
        byte = self.__serialport.read()
        if not byte:
            return 0
        data = ord(byte)
        if data == ANALOG_READ:
            data = ord(self.__serialport.read())
            if data == pin:
                analog_val = int((ord(self.__serialport.read()) << 8) + ord(self.__serialport.read())) 
                if self.__device == ARDUINO:
                    value = round(float(analog_val / 1023),4)
                else:
                    value = round(float(analog_val / 4095),4)
                return value
        return 0
    def attachServo(self, pin: int):
        self.__serialport.write(bytearray([SERVO_CONFIG,pin,0,0]))
    def servoWrite(self, angle: int):
        angle = max(0, min(angle, 180))
        self.__serialport.write(bytearray([SERVO_WRITE,0,0,angle]))
    def close(self):
        self.__serialport.close()
        