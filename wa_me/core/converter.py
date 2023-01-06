#!/usr/bin/env python

from dataclasses import asdict
from enum import Enum
from typing import Any, Dict, TypeVar, Type

import dacite

__all__ = ("as_dict", "from_dict")

T = TypeVar("T")
config = dacite.Config(cast=[Enum])


def _as_dict(_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        k
        if k != "sender"
        else "from": (
            v.value
            if isinstance(v, Enum)
            else _as_dict(v)
            if isinstance(v, dict)
            else [_as_dict(_v) for _v in v]
            if isinstance(v, list)
            else tuple([_as_dict(_v) for _v in v])
            if isinstance(v, tuple)
            else v
        )
        for k, v in _data.items()
        if v is not None
    }


def _from_dict(_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        k
        if k != "from"
        else "sender": (
            _from_dict(v)
            if isinstance(v, dict)
            else [_from_dict(_v) for _v in v]
            if isinstance(v, list)
            else tuple([_from_dict(_v) for _v in v])
            if isinstance(v, tuple)
            else v
        )
        for k, v in _data.items()
    }


def as_dict(data: T) -> Dict[str, Any]:
    """Create a dictionary from a data class instance.

    Parameters
    ----------
    data: :class:`Type[T]`
        An instance of a data class.

    Returns
    -------
    Dict[:class:`str`, Any]
        A dictionary mapping field names to field values of a input dataclass
        instance.
    """
    return _as_dict(asdict(data))


def from_dict(data_class: Type[T], data: Dict[str, Any]) -> T:
    """Create a data class instance from a dictionary.

    Parameters
    ----------
    data_class: :class:`Type[T]`
        A data class type.
    data: Dict[:class:`str`, Any]
        A dictionary of a input data.

    Returns
    -------
    :class:`T`
        An instance of a data class.
    """
    return dacite.from_dict(data_class=data_class, data=_from_dict(data), config=config)
