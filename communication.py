import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('COM11', 57600, timeout=1)
    ser.flush()

    while True:
        #ser.write(b"Hello from Raspberry Pi!\n")
        # ser.write("Hello from Visual Studio Code!\n".encode('utf-8'))
        # line = ser.readline().rstrip()
        line = ser.readline()
        print(line)
        time.sleep(1)