#include "simplecontroller.h"

int main()
{
    Board *b = connectDevice("/dev/cu.usbmodem14101", B115200);
    // b->pinMode(b, 2, OUTPUT);
    // b->pinMode(b, 13, INPUT_PULLUP);
    // bool val;
    uint angle = 0;
    b->attachServo(b, 9);
    while (1)
    {
        b->servoWrite(b, angle);
        angle += 10;
        if (angle > 180)
            angle = 0;

        // val = b->digitalRead(b, 13);
        // b->digitalWrite(b, 2, val);
        // printf("%f\n", b->analogRead(b, 13));
        // b->analogWrite(b, 2, b->analogRead(b, 13));

        Sleep(1000);
        // b->digitalWrite(b, 2, 0);
        // Sleep(1000);
    }

    b->closeDevice(b);
    return 0;
}
