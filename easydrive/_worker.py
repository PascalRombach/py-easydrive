from threading import Thread
from concurrent.futures import Future as ConcurrentFuture
from typing import Any, Optional, Callable
from asyncio import new_event_loop, Future as AIOFuture, run_coroutine_threadsafe

__all__ = (
    "AsyncWorker",
    "get_single_worker"
)

class AsyncWorker(Thread):
    def run(self):
        self._loop = new_event_loop()

        self._loop.run_forever()
        pass

    def run_future(self, 
        future: AIOFuture, 
        blocking: bool=True, 
        completion_callback: Callable[[ConcurrentFuture],None]= None, 
        timeout: Optional[float]=None
        ) -> ConcurrentFuture|Any:
        con_future: ConcurrentFuture = run_coroutine_threadsafe(future)
        
        if completion_callback is not None:
            con_future.add_done_callback(completion_callback)
            pass
        
        if blocking: 
            return con_future.result(timeout)
            pass
        else:
            return con_future
            pass
        pass
    pass


_SINGLE: AsyncWorker = ...
def get_single_worker():
    global _SINGLE

    if _SINGLE is Ellipsis:
        _SINGLE= AsyncWorker()
        _SINGLE.start()
        pass

    return _SINGLE
    pass