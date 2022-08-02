# from __future__ import print_function
from dronekit import connect, VehicleMode
import time
import sys
import serial
# from __future__ .import print_function
from builtins import object
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2

if __name__ == '__main__':
    ser = serial.Serial('COM16', 57600, timeout=1)
    ser.flush()
    
class fifo(object):
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf += data
        return len(data)
    def read(self):
        return self.buf.pop(0)

vehicle = connect('COM11', wait_ready=True)
vehicle.wait_ready('autopilot_version')

def test_protocol(mavlink,data_, signing=False):
    f = fifo()
    mav = mavlink.MAVLink(f)
    if signing:
        mav.signing.secret_key = bytearray(chr(42)*32, 'utf-8' )
        mav.signing.link_id = 0
        mav.signing.timestamp = 0
        mav.signing.sign_outgoing = True

    mav.param_set_send(1, 1, b"hdg", data_, mavlink.MAV_PARAM_TYPE_INT16)
    m = mav.param_set_encode(1, 1, b"hdg", data_, mavlink.MAV_PARAM_TYPE_INT16)
    m.pack(mav)
    b = m.get_msgbuf()

    bi=[]
    for c in b:
        bi.append(int(c))
    
    ser.write(str(bi).encode('utf-8'))
    print("Data Sent")
    print(bi)

while 1:
    print(" Heading: %s" % vehicle.heading)
    test_protocol(mavlink1,vehicle.heading)
    time.sleep(1)
