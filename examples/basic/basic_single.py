from easydrive import Controller
from time import sleep

controller = Controller()           # This is the controller. It manages the vehicles for us
v = controller.connect_one()        # Connect to one non-charging vehicle

v.set_speed(300)                    # Let the vehicle drive at 300mm/s

sleep(10)                           # Sleep for 10s

v.stop()                            # Stop the vehicle
v.disconnect()                      # Disconnect from the vehicle. This is neccessary so that the vehicles don't freak out
