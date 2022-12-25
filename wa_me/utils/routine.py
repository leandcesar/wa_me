import time
from functools import wraps
from threading import Timer
from typing import Any, Callable, TypeVar


class Routine:
    def __init__(self, callback: Callable, interval: float, *args, **kwargs) -> None:
        self._timer: Timer = None
        self._next: float = None
        self._callback = callback
        self._interval = interval
        self._running = False
        self._args = args
        self._kwargs = kwargs

    def loop(self) -> None:
        self._running = False
        self.start()
        self._callback(*self._args, **self._kwargs)

    def start(self) -> None:
        if self._running:
            raise Exception()  # TODO
        if self._next is None:
            self._next = time.time()
        self._next += self._interval
        self._timer = Timer(self._next - time.time(), self.loop)
        self._timer.start()
        self._running = True

    def stop(self) -> None:
        if not self._running:
            raise Exception()  # TODO
        self._timer.cancel()
        self._running = False


def routine(seconds: float) -> Callable[[Callable[..., Any]], Routine]:
    def decorator(func: Callable[..., Any]) -> Routine:
        @wraps(func)
        def wrapped(*args, **kwargs) -> Routine:
            return Routine(func, seconds, *args, **kwargs)

        return wrapped(func)

    return decorator
