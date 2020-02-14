from attr import attrs, attrib

from aioalice.utils import ensure_cls, safe_kwargs
from . import AliceObject, MediaButton


@safe_kwargs
@attrs
class CardFooter(AliceObject):
    """This object represents a card's footer"""
    text = attrib(type=str)
    button = attrib(default=None, convert=ensure_cls(MediaButton))
