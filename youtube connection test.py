from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import socket
# import exceptions
import math
import argparse


def connectMyCopter():
#     parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
#     parser.add_argument('--connect',
#                         help="Vehicle connection target string. If not specified, SITL automatically started and used.")
#     args = parser.parse_args()

#     connection_string = args.connect
#     sitl = None

#     if not connection_string:
#         import dronekit_sitl
#         sitl = dronekit_sitl.start_default()
#         connection_string = sitl.connection_string()


# # Connect to the Vehicle
#     print('Connecting to vehicle on: %s' % connection_string)
#     vehicle = connect(connection_string, wait_ready=True)

    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parser_args()

    connection_string = args.connect
    baud_rate = 57600

    vehicle = connect(connection_string,baud = baud_rate,wait_ready= True)
    return vehicle

def arm():
    while vehicle.is_armable ==False:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    print("Your Vehicle is now armable")

    vehicle.armed = True
    while vehicle.armed ==False:
        print("Waiting for vehicle to become armed...")
        time.sleep(1)

    print("Vehicle is now armed...")
    print("probs are spinningggggg...")

    return None

vehicle = connectMyCopter()
arm()
print("Endd.......")