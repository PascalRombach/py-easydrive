from time import sleep
from easydrive import Controller

controller = Controller()
vehicles = controller.connect_many(2)

for v in vehicles:
    v.set_speed(300)

sleep(10)

for v in vehicles:
    v.stop()

controller.disconnect_all()