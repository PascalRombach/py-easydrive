from time import sleep
from easydrive import Controller

controller = Controller()               # This is the controller. It manages the vehicles for us
vehicles = controller.connect_many(2)   # Connect to one non-charging vehicle

for v in vehicles:                      # Loop through all vehicles
    v.set_speed(300)                    # and make every vehicle drive at 300mm/s

sleep(10)                               # Sleep for 10s

for v in vehicles:                      # Loop through all vehicles (again)
    v.stop()                            # and stop every vehicle

controller.disconnect_all()             # Disconnect from all vehicles.
# Alternatively you could do the following:
# for v in vehicles:
#     v.disconnect()