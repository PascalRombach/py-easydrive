from typing import Callable, Optional
from .._worker import get_single_worker
from anki import Vehicle as AVehicle, TrackPiece
from anki.utility.lanes import _Lane, Lane3, Lane4

class Vehicle:
    def __init__(self, vehicle: AVehicle):
        self._internal = vehicle
        pass

    def wait_for_track_change(self, timeout: Optional[float]=None) -> Optional[TrackPiece]:
        return get_single_worker().run_future(
            self._internal.wait_for_track_change(),
            timeout=timeout
        )
        pass

    def disconnect(self, 
        blocking: bool=True,
        timeout: Optional[float]=None,
        completion_callback: Callable[[],None]=None
        ) -> bool:
        result = get_single_worker().run_future(
            self._internal.disconnect(),
            blocking=blocking,
            completion_callback=completion_callback,
            timeout=timeout
        )

        if blocking:
            return result
        pass

    def set_speed(self, 
        speed: int, 
        acceleration: int=500
        ):
        get_single_worker().run_future(
            self._internal.setSpeed(speed,acceleration),
            False
        )
        pass

    def stop(self):
        get_single_worker().run_future(
            self._internal.stop(),
            False
        )
        pass

    def change_lane(self, 
        lane: _Lane, 
        horizontal_speed: int=300, 
        horizontal_acceleration: int=300
        ):
        get_single_worker().run_future(
            self._internal.changeLane(lane,horizontal_speed,horizontal_acceleration)
        )
        pass

    def change_position(self,
        road_center_offset: float,
        horizontal_speed: int=300,
        horizontal_acceleration: int=300
        ):
        get_single_worker().run_future(
            self._internal.changePosition(road_center_offset,horizontal_speed,horizontal_acceleration)
        )
        pass

    def turn(self):
        get_single_worker().run_future(
            self._internal.turn()
        )
        pass

    def get_lane(self, mode: type[_Lane]):
        return self._internal.getLane(mode)
        pass

    def align_to_start(self, 
        speed: int=300,
        blocking: bool=True,
        completion_callback: Callable[[],None]=None,
        ):
        get_single_worker().run_future(
            self._internal.align(speed),
            blocking,
            (lambda _: completion_callback()) 
            if completion_callback is not None 
            else None
        )
        pass

    
    def track_piece_change(self, func):
        self._internal.trackPieceChange(func)
        pass

    def remove_track_piece_watcher(self, func):
        self._internal.removeTrackPieceWatcher(func)
        pass

    
    # These properties just translate from the py-drivesdk.
    # Sadly, there is no easy way to automate this
    @property
    def is_connected(self) -> bool:
        return self._internal.is_connected
    
    @property
    def current_track_piece(self) -> TrackPiece:
        return self._internal.current_track_piece
    
    @property
    def map(self) -> tuple[TrackPiece]:
        return self._internal.map
    
    @property
    def map_position(self) -> int:
        return self._internal.map_position
    
    @property
    def road_offset(self) -> float:
        return self._internal.road_offset
    
    @property
    def speed(self) -> int:
        return self._internal.speed
    
    @property
    def current_lane3(self) -> Optional[Lane3]:
        return self._internal.current_lane3
    
    @property
    def current_lane4(self) -> Optional[Lane4]:
        return self._internal.current_lane4
    
    @property
    def id(self) -> int:
        return self._internal.id
    pass

