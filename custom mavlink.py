from __future__ import print_function
from builtins import object
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2

class fifo(object):
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf += data
        return len(data)
    def read(self):
        return self.buf.pop(0)

def test_protocol(mavlink, signing=False):
    f = fifo()
    print("Creating MAVLink message...")
    
    mav = mavlink.MAVLink(f)
    if signing:
        mav.signing.secret_key = bytearray(chr(42)*32, 'utf-8' )
        mav.signing.link_id = 0
        mav.signing.timestamp = 0
        mav.signing.sign_outgoing = True

# target_system : the MAVLink system id of the vehicle (normally “1”)
# target_components : normally “1”
# param_id : the human readable 16 character parameter name
# param_value : the new value for the parameter expressed as a float
# param_type : the MAV_PARAM_TYPE for the parameter. This must match the type of the parameter within the AutoPilot and will be MAV_PARAM_TYPE_INT8, MAV_PARAM_TYPE_INT16, MAV_PARAM_TYPE_INT32 or MAV_PARAM_TYPE_REAL32 (the only types that ArduPilot supports). It may be convenient to store the “param_type” field from the PARAM_VALUE message sent by the flight controller for this parameter.

# target_system : 7, target_component : 1, param_id : test, param_value : 101.0, param_type : 9
    mav.param_set_send(1, 1, b"test", 101, mavlink.MAV_PARAM_TYPE_INT8)
    m = mav.param_set_encode(1, 1, b"test", 101, mavlink.MAV_PARAM_TYPE_INT8)
    m.pack(mav)
    b = m.get_msgbuf()

    bi=[]
    for c in b:
        bi.append(int(c))
    print("Buffer containing the encoded message:")
    print(bi)

    print("Decoding message...")
    m2 = mav.decode(b)
    # print("Got a message with id %u and fields %s" % (m2.get_msgId(), m2.get_fieldnames()))
    print(m2)


print("Testing mavlink1\n")
test_protocol(mavlink1)

print("\nTesting mavlink2\n")
test_protocol(mavlink2)

print("\nTesting mavlink2 with signing\n")
test_protocol(mavlink2, True)