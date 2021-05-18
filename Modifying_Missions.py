from dronekit import connect,VehicleMode,Command
from pymavlink import mavutil

vehicle=connect("127.0.0.1:14550",wait_ready=True)

cmds=vehicle.commands
cmds.download()
cmds.wait_ready()

missionlist=[] # creating an array of missions

for c in cmds:
    missionlist.append(c)

#to modify any of the missions
missionlist[0].command=mavutil.mavlink.MAV_CMD_NAV_TAKEOFF

#clearing the current missions
cmds.clear()

#uploading the missions
for c in missionlist:
    cmds.add(c)
cmds.upload()