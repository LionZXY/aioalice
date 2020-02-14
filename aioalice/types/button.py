from attr import attrs, attrib

from . import AliceObject
from ..utils import safe_kwargs


@safe_kwargs
@attrs
class Button(AliceObject):
    """Button object"""
    title = attrib(type=str)
    url = attrib(default=None, type=str)
    payload = attrib(default=None)
    hide = attrib(default=True, type=bool)
