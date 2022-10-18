from easydrive import Controller, TrackPieceTypes

controller = Controller()
vehicle = controller.connect_one()

controller.scan()

vehicle.set_speed(300)
vehicle.wait_for_track_change()
try:
    while vehicle.current_track_piece.type != TrackPieceTypes.START:
        vehicle.wait_for_track_change()
        print(
            "This vehicle is currently on",
            vehicle.current_track_piece.type,
            "at position",
            vehicle.map_position
        )
        pass
finally:
    vehicle.stop()
    vehicle.disconnect()