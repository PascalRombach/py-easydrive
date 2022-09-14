from easydrive import Controller
from time import sleep

controller = Controller()
v = controller.connect_one()

v.set_speed(300)

sleep(10)

v.stop()
v.disconnect()
