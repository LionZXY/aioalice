from attr import attrs, attrib

from . import AliceObject
from ..utils import safe_kwargs


@safe_kwargs
@attrs
class EntityTokens(AliceObject):
    """EntityTokens object"""
    start = attrib(type=int)
    end = attrib(type=int)
