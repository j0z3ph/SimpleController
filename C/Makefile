COMPILER=gcc
SERIAL=serial.c
SERIAL_H=serial.h

run: test.exe
	./test.exe

test.exe: lectura_analog.c $(SERIAL_H)
	$(COMPILER) -o test.exe lectura_analog.c $(SERIAL)

