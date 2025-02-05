#include <stdio.h>
#include <stdbool.h>
#include "serial.h"

#define DIGITAL_READ 0x80
#define DIGITAL_WRITE 0x81
#define ANALOG_READ 0x82
#define ANALOG_WRITE 0x83
#define SERVO_WRITE 0x84
#define SERVO_CONFIG 0x85
#define SET_PIN_MODE 0x86
#define RESET_MESSAGE 0xFF
#define DEVICE_INFO 0xF0

#define ARDUINO 0
#define ESP32 1

typedef struct Board
{
    const unsigned int INPUT;
    const unsigned int OUTPUT;
    const unsigned int SERVO;
    const unsigned int INPUT_PULLUP;
    SerialPort *sp;
    void (*pinMode)(struct Board *self, unsigned int pin, unsigned int mode);
    void (*digitalWrite)(struct Board *self, unsigned int pin, bool value);
    void (*analogWrite)(struct Board *self, unsigned int pin, float value);
    void (*digitalRead)(struct Board *self, unsigned int pin);
    float (*analogRead)(struct Board *self, unsigned int pin);
    void (*attachServo)(struct Board *self, unsigned int pin);
    void (*servoWrite)(struct Board *self, unsigned int angle);
    void (*close)(struct Board *self);
    

} Board;

Board *connect(const char *portName, BaudRate baudrate);

void pinMode(Board *self, unsigned int pin, unsigned int mode);
void digitalWrite(Board *self, unsigned int pin, bool value);
void analogWrite(Board *self, unsigned int pin, float value);
bool digitalRead(Board *self, unsigned int pin);
float analogRead(Board *self, unsigned int pin);
void attachServo(Board *self, unsigned int pin);
void servoWrite(Board *self, unsigned int angle);
void close(Board *self);

int main()
{
    Board b;
    return 0;
}
