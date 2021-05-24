from dronekit import connect, VehicleMode , LocationGlobalRelative , Command
from pymavlink import mavutil
from time import sleep
import tkinter as tk

print("Connecting...")
vehicle=connect("udp:127.0.0.1:14550",wait_ready=True)
print("Connected")

def arm_and_takeoff():
    takeoff_alt=10
    while not vehicle.is_armable:
        print("Waiting to initialize...")
        sleep(1)
    vehicle.mode=VehicleMode("GUIDED")
    vehicle.armed=True
    while not vehicle.armed:
        print("Waiting for vehicle to get armed")
        sleep(1)
    print("Vehicle armed...Ready for Take off")
    vehicle.simple_takeoff(takeoff_alt)
    while True:
            print("altitude: {val}".format(val=vehicle.location.global_relative_frame.alt))
            if vehicle.location.global_relative_frame.alt>=takeoff_alt*0.95:
                print("target altitude reached")
                break
            sleep(1)

def send_body_ned_velocity(velocity_x,velocity_y,velocity_z,duration):
    msg=vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_NED, # frame Needs to be MAV_FRAME_BODY_NED for forward/back left/right control.
        0b0000111111000111, # type_mask bitmask,,consider only the velocities
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # m/s
        0, 0, 0, # x, y, z acceleration
        0, 0)
    for x in range(duration):
        vehicle.send_mavlink(msg)
        vehicle.flush()

#binding the drone to keyboard using tkinter
#key event function
def key(event):
    ##keysym : A single-character string that is the key's code (only for keyboard events)
    ##char : A string that is the key's symbolic name (only for keyboard events)
    if event.char==event.keysym:  
        if event.keysym == 'r':
            vehicle.mode=VehicleMode("RTL") ##land the drone
    else:
        if event.keysym=='Up':
            send_body_ned_velocity(0,100,0,1)
        elif event.keysym=='Down':
            send_body_ned_velocity(0,-100,0,1)
        elif event.keysym=='Left':
            send_body_ned_velocity(-100,0,0,1)
        elif event.keysym=='Right':
            send_body_ned_velocity(100,0,0,1)


arm_and_takeoff()

#Reading the keyboard using tkinter
root=tk.Tk()
print("Control the drone using your arrow keys")
print("Press R for RTL mode")
root.bind_all("<Key>",key)
root.mainloop() #infinite while loop
