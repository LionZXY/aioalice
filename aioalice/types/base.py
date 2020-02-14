from attr import attrs, asdict

from aioalice.utils import safe_kwargs


@safe_kwargs
@attrs
class AliceObject(object):
    """AliceObject is base class for all Alice requests related objects"""

    def to_json(self):
        return asdict(self)
