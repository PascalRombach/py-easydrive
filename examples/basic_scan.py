from easydrive import Controller

control = Controller()                      # This is the controller. It manages the vehicles for us
v = control.connect_one()                   # Connect to one non-charging vehicle

control.scan(v)                             # Scan in the track. This is required for everything
                                            # you want to do that somehow interacts with the track

v.set_speed(300)                            # Make the vehicle drive at 300mm/s
try:
    while True:
        print(v.wait_for_track_change())    # Print out every track piece the vehicle drives across
        pass
    pass
except KeyboardInterrupt:                   # Handle ^C
    control.disconnect_all()                # by disconnecting every vehicle (although there's just one)
    pass
