from attr import attrs, attrib

from . import AliceObject
from ..utils import safe_kwargs


@safe_kwargs
@attrs
class CardHeader(AliceObject):
    """This object represents a card's header"""
    text = attrib(type=str)
