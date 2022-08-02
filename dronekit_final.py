# from __future__ import print_function
from dronekit import connect, VehicleMode
import time
import sys

vehicle = connect('COM11', wait_ready=True)

vehicle.wait_ready('autopilot_version')

while 1:
    # print(vehicle.location.global_relative_frame.lat)
    # print(vehicle.location.global_relative_frame.lon)
    # print(vehicle.location.global_relative_frame.alt)
    print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    print(" Attitude: %s" % vehicle.attitude)
    print(" Velocity: %s" % vehicle.velocity)
    print(" Battery: %s" % vehicle.battery)
    print(" EKF OK?: %s" % vehicle.ekf_ok)
    print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
    print(" Rangefinder: %s" % vehicle.rangefinder) #optional
    print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)#optional
    print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)#optional
    print(" Heading: %s" % vehicle.heading)
    print(" System status: %s" % vehicle.system_status.state)
    print(" Groundspeed: %s" % vehicle.groundspeed)    
    print(" Airspeed: %s" % vehicle.airspeed)    
    print("")

    total_size = (sys.getsizeof(vehicle.location.global_relative_frame)
    +sys.getsizeof(vehicle.attitude)
    +sys.getsizeof(vehicle.velocity)
    +sys.getsizeof(vehicle.battery)
    +sys.getsizeof(vehicle.ekf_ok)
    +sys.getsizeof(vehicle.last_heartbeat)
    +sys.getsizeof(vehicle.rangefinder)
    +sys.getsizeof(vehicle.rangefinder.distance)
    +sys.getsizeof(vehicle.rangefinder.voltage)
    +sys.getsizeof(vehicle.heading)
    +sys.getsizeof(vehicle.system_status.state)
    +sys.getsizeof(vehicle.groundspeed)
    +sys.getsizeof(vehicle.airspeed)
    )
    
    print(" Total size : "+str(total_size) + " bytes")
    print("")
    print("")
    print("")
    time.sleep(2)
