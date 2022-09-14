from concurrent.futures import Future
from typing import Iterable, Optional, Callable
from anki import Controller as AController, Vehicle as AVehicle, TrackPiece

from .._worker import get_single_worker
from .vehicle import Vehicle

async def _wrap_vehicle(v: AVehicle):
        # Wraps py-drivesdk's Vehicle object into ours. This is done in an async function to make sure the event listener register there
        return Vehicle(v)
        pass

class Controller:
    def __init__(self,*, timeout: float=10):
        self._internal= AController(timeout=timeout)
        pass

    def connect_one(self, vehicle_id: Optional[int]=None) -> Vehicle:
        worker = get_single_worker()
        return worker.run_future(_wrap_vehicle(worker.\
            run_future(self._internal.connectOne(vehicle_id))))
        pass

    def connect_specific(self, address: str, vehicle_id: Optional[int]=None) -> Vehicle:
        worker = get_single_worker()
        return worker.run_future(_wrap_vehicle(worker.\
            run_future(self._internal.connectSpecific(address,vehicle_id))))
        pass

    def connect_many(self, amount: int, vehicle_ids: Iterable[int]=None) -> tuple[Vehicle]:
        worker = get_single_worker()
        return tuple([worker.run_future(_wrap_vehicle(v))
            for v in worker.\
                run_future(self._internal.connectMany(amount,vehicle_ids))])
        pass

    def scan(self, 
        scan_vehicle: Vehicle, 
        align_pre_scan: bool=True, 
        blocking: bool=True, 
        completion_callback: Callable[[list[TrackPiece]],None]=None
        ) -> list[TrackPiece]:
        def callback(future: Future):
            completion_callback(future.result())

        return get_single_worker().run_future(
            self._internal.scan(scan_vehicle._internal,align_pre_scan),
            blocking,
            callback if completion_callback is not None else None
            )
        pass

    def disconnect_all(self, 
        blocking: bool=True, 
        completion_callback: Callable[[],None]=None):
        get_single_worker().run_future(
            self._internal.disconnectAll(),
            blocking,
            (lambda _: completion_callback()) 
            if completion_callback is not None 
            else None
        )
        pass

    @property
    def map_types(self) -> tuple:
        return self._internal.map_types
        pass


    def __enter__(self):
        return self
        pass

    def __exit__(self,*args):
        self.disconnect_all()
        pass
    pass