from __future__ import print_function
from dronekit import connect, VehicleMode
import time
import sys

vehicle = connect('COM16', wait_ready=True)

vehicle.wait_ready('autopilot_version')

while 1:
    print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    print(" ALtitude: %s" % vehicle.location.global_relative_frame.alt)
    print(" Attitude: %s" % vehicle.attitude)
    print(" Velocity: %s" % vehicle.velocity)
    print(" Battery: %s" % vehicle.battery)
    print(" EKF OK?: %s" % vehicle.ekf_ok)
    print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
    print(" Rangefinder: %s" % vehicle.rangefinder)
    print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)
    print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
    print(" Heading: %s" % vehicle.heading)
    print(" System status: %s" % vehicle.system_status.state)
    print(" Groundspeed: %s" % vehicle.groundspeed)    # settable
    print(" Airspeed: %s" % vehicle.airspeed)    # settable
    print("")
    total_size = sys.getsizeof(vehicle.location.global_relative_frame)+sys.getsizeof(vehicle.attitude)
    print("Total size : "+str(total_size) + " bytes")
    print("")
    print("")
    print("")
    time.sleep(2)
