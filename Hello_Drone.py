#Drone-kit python script

from dronekit import connect,VehicleMode

print("Start simulator (SITL)")

#connecting to the vehicle
print("Waiting to connect to the vehicle on: %s" %('127.0.0.1:14550'))
vehicle=connect('127.0.0.1:14550',wait_ready=True)

#getting different states of the vehicle
print("Getting some vehicle attributes:")
print("GPS: %s" %(vehicle.gps_0)) #get GPS location
print("Battery: %s" %(vehicle.battery)) #get battery status
print("Last Heartbeat: %s" %(vehicle.last_heartbeat))  #Time since last MAVLink heartbeat was received 
print("Is vehicle armable? %s" %(vehicle.is_armable))
print("System Status: %s" %(vehicle.system_status.state)) #refer https://dronekit.netlify.app/automodule.html#dronekit.Vehicle.system_status
print("Mode: %s" %(vehicle.mode.name))

#closing the vehicle object before exiting the script
vehicle.close()
