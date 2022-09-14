from easydrive import Controller
from time import sleep

control = Controller()
v = control.connect_one()

control.scan(v)

v.set_speed(300)
try:
    while True:
        print(v.wait_for_track_change())
        pass
    pass
except KeyboardInterrupt:
    control.disconnect_all()
    pass
