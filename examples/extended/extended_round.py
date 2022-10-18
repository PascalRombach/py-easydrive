from easydrive import Controller, TrackPieceTypes

controller = Controller()                                               # The controller manages all vehicles
vehicle = controller.connect_one()                                      # Connect to one non-charging supercar

controller.scan()                                                       # Scan in the track. We need to do this
                                                                        # whenever we access the map

vehicle.set_speed(300)                                                  # Start driving after the scan at 300mm/s
vehicle.wait_for_track_change()                                         # Waits until the vehicle has entered a new track piece
                                                                        # Since we are doing this we skip the START piece
try:
    while vehicle.current_track_piece.type != TrackPieceTypes.START:    # Loop until we enter the START piece
        vehicle.wait_for_track_change()                                 # Wait until entering a new piece
        print(                                                          # Print out the current position
            "This vehicle is currently on",
            vehicle.current_track_piece.type,
            "at position",
            vehicle.map_position
        )
        pass
finally:
    vehicle.stop()
    vehicle.disconnect()