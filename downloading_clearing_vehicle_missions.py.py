from dronekit import connect,VehicleMode

vehicle=connect("127.0.0,1:14450",wait_ready=True)

#downloading current mission
#download the current waypoints
cmds=vehicle.commands #get the waypoints
cmds.download() #download the way points
cmds.wait_ready() #wait until the download is complete

#clearing the current mission
cmds.clear() #clearing all the waypoints
cmds.upload() #uploading the command to the vehicle

