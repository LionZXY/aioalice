from attr import attrs, attrib

from . import AliceObject
from ..utils import safe_kwargs


@safe_kwargs
@attrs
class MediaButton(AliceObject):
    """MediaButton object"""
    text = attrib(type=str)
    url = attrib(type=str)
    payload = attrib(default=None)
