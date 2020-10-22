import importlib
from dataclasses import dataclass, field
from enum import Enum
from ipaddress import IPv4Address
from typing import Any, List

from ndk.exceptions import IntegrityError


@dataclass
class Field:
    primary_key: bool = False
    composite_key: bool = False
    required: bool = False
    default: str = None
    field_type: type = None

    def __post_init__(self):
        if self.default is not None and self.field_type is not None:
            self.default = self.serializer(self.default)

    @staticmethod
    def normalize_name(name):
        return str(name).lower().replace(' ', '-')

    def serializer(self, value):
        return self.field_type(value)


@dataclass
class StringField(Field):
    field_type: str = str


@dataclass
class IntegerField(Field):
    field_type: int = int


@dataclass
class BooleanField(Field):
    field_type: bool = bool

    def serializer(self, value):
        """Nagios Object use [0/1] to represent the Boolean value"""
        if self.field_type(value):
            return 1
        return 0


@dataclass
class Ipv4Field(Field):
    field_type: IPv4Address = IPv4Address


@dataclass
class ChoiceField(Field):
    field_type: List[str] = field(default_factory=list)
    choices: Enum = None

    def __post_init__(self):
        if self.primary_key:
            raise IntegrityError('ChoiceField can not be a Primary Key')
        if not self.choices:
            raise IntegrityError('`.choices` is required in ChoiceField')
        if not issubclass(self.choices, Enum):
            raise IntegrityError('`.choices` must be Enum instance')
        super().__post_init__()

    def serializer(self, value):
        if value:
            if not isinstance(value, list):
                value = [value]
            return ','.join((x.value for x in value))
        return value


@dataclass
class ForeignKey(Field):
    field_type: type = str
    relation: str = None

    def __post_init__(self):
        if not self.relation:
            raise IntegrityError('.relation is requried field in ForeignKey')
        super().__post_init__()

    def serializer(self, obj):
        module = importlib.import_module('.objects', package='ndk')
        relation = getattr(module, self.relation)
        if not isinstance(obj, relation):
            raise IntegrityError(
                f'{obj} object must be a {relation} instance.')
        return self.field_type(obj)
