#!/usr/bin/env python
from __future__ import annotations

from collections import OrderedDict
from threading import RLock
from time import time
from typing import Any, Iterator, List, Optional, Tuple

__all__ = ("TTLDict",)


class TTLDict(OrderedDict):
    """OrderedDict with key expiry time."""

    def __init__(
        self,
        max_len: Optional[int] = None,
        ttl: Optional[int] = None,
        reset_on_get: Optional[bool] = None,
        *args,
        **kwargs,
    ) -> None:
        assert max_len is None or (isinstance(max_len, int) and max_len >= 1)
        assert ttl is None or (isinstance(ttl, int) and ttl >= 0)
        assert reset_on_get is None or isinstance(reset_on_get, bool)

        self._max_len = max_len
        self._ttl = ttl
        self._reset_on_get = reset_on_get
        self._lock = RLock()

        OrderedDict.__init__(self)
        self.update(*args, **kwargs)

    def __contains__(self, k: Any) -> bool:
        with self._lock:
            try:
                v, _time = OrderedDict.__getitem__(self, k)
                if time() - _time < self._ttl:
                    return True
                del self[k]
            except KeyError:
                pass
        return False

    def __delitem__(self, k: str) -> Any:
        with self._lock:
            OrderedDict.__delitem__(self, k)

    def __getitem__(self, k: str) -> Any:
        with self._lock:
            v, _time = OrderedDict.__getitem__(self, k)
            if time() - _time < self._ttl:
                if self._reset_on_get:
                    del self[k]
                    OrderedDict.__setitem__(self, k, (v, time()))
                return v
            del self[k]
            raise KeyError(k)

    def __len__(self) -> int:
        with self._lock:
            return OrderedDict.__len__(self)

    def __setitem__(self, k: str, v: Any) -> None:
        with self._lock:
            if self._max_len is not None and len(self) == self._max_len:
                if k in self:
                    del self[k]
                else:
                    try:
                        self.popitem(last=False)
                    except KeyError:
                        pass
            OrderedDict.__setitem__(self, k, (v, time()))

    def get(self, k: str, default: Any = None) -> Any:
        try:
            return self[k]
        except KeyError:
            return default

    def pop(self, k: str, default: Any = None) -> Any:
        try:
            v = self[k]
        except KeyError:
            return default
        else:
            del self[k]
            return v

    def items(self) -> List[Tuple[str, Any]]:
        return [(k, self[k]) for k in list(self.keys()) if k in self]

    def values(self) -> List[Any]:
        return [self[k] for k in list(self.keys()) if k in self]

    def copy(self) -> TTLDict:
        s = OrderedDict.copy(self)
        s._max_len = self._max_len
        s._ttl = self._ttl
        return s
