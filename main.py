# from __future__ import print_function
from tkinter.tix import Tree
from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
import sys

maxRoll = 10.0
maxYaw = 10.0
maxPitch = 10.0
minGroundSpeed = 0.0

timerCount = 0
waitTime = 5
deployParachuteStatus = False

vehicle = connect('COM11', wait_ready=True)

vehicle.wait_ready('autopilot_version')

# print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
# print(" Attitude: %s" % vehicle.attitude)
# print(" Velocity: %s" % vehicle.velocity)
# print(" Battery: %s" % vehicle.battery)
# print(" EKF OK?: %s" % vehicle.ekf_ok)
# print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
# print(" Rangefinder: %s" % vehicle.rangefinder) #optional
# print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)#optional
# print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)#optional
# print(" Heading: %s" % vehicle.heading)
# print(" System status: %s" % vehicle.system_status.state)
# print(" Groundspeed: %s" % vehicle.groundspeed)
# print(" Airspeed: %s" % vehicle.airspeed)


def deployParachute():
    global deployParachuteStatus

    deployParachuteStatus = True
    print("Parachute Deployed")


def checkCompassData():
    pass


def checkGpsData():
    if(str(vehicle.location.global_relative_frame.lat) == "0.0" or str(vehicle.location.global_relative_frame.lon) == "0.0"):
        return False
    else:
        return True


def calculatePredictedRange():
    pass


def calculateActualRange():
    pass


def sendMessage():
    pass


def changeMode():
    pass


def checkRoll():
    if(float(vehicle.attitude.roll) > maxRoll):
        return False
    else:
        return True


def checkYaw():
    if(float(vehicle.attitude.yaw) > maxRoll):
        return False
    else:
        return True


def checkPitch():
    if(float(vehicle.attitude.pitch) > maxRoll):
        return False
    else:
        return True


def checkWindSpeed():
    pass


def checkTemperature():
    pass


def checkGroundSpeed():
    if(float(vehicle.groundspeed) < minGroundSpeed):
        return False
    else:
        return True

def stopWholeSystem():
    pass

def landing():
    point1 = LocationGlobalRelative(27.68467379391221, 85.28458431218176, 20)
    vehicle.simple_goto(point1)

landing()
# while 1:
#     if(checkGroundSpeed() or checkGpsData()):
#         timerCount = 0
#         print("EveryThing is Good")
#     else:
#         if (not deployParachuteStatus):
#             timerCount = timerCount + 1
#             print("start timer : "+ str(timerCount))
#             time.sleep(1)

#     if(timerCount == waitTime):
#         timerCount = 0 
#         deployParachute()

