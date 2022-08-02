import serial 
import RPi.GPIO as GPIO
import os,time

GPIO.setmode(GPIO.BOARD)

ser = serial.Serial("/dev/ttyAMA0",baudrate = 9600,timeout = 1)

ser.write('AT'+'\r\n')
# rcv = ser.read(10)
# print(rcv)
time.sleep(1)

ser.write("AT+CPIN?\r")
# msg = ser.read(128)
# print(msg)
time.sleep(1)


ser.write("AT+CREG?\r")
# msg = ser.read(128)
# print(msg)
time.sleep(1)

ser.write("AT+CGATT?\r")
# msg = ser.read(128)
# print(msg)
time.sleep(1)



ser.write("AT+CIPSHUT\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIPSTATUS?\r")
# msg = ser.read(128)
# print(msg)
time.sleep(1)

ser.write("AT+CIPMUX=0\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CSTT=\"ntnet\"\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIICR\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIFSR\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIPSPRT=0\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIPSEND\r")
msg = ser.read(128)
print(msg)
time.sleep(1)

ser

distance = "data"

command = "GET https://api.thingspeak.com/update?api_key=TNPMHK9DYSK0G6EC&field1=" + str(distance)
# command = "AT+CGDCONT=1"+","+'"IP"'+","'"internet.ooredoo.tn"\r'
ser.write(command.encode())
msg = ser.read(128)
print(msg)
time.sleep(1)

ser.write("AT+CIPSHUT\r")
msg = ser.read(128)
print(msg)
time.sleep(1)