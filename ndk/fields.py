from dataclasses import dataclass, field
from ipaddress import IPv4Address, ip_address


@dataclass
class Field:
    primary_key: bool = False
    composite_key: bool = False
    requried: bool = False
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
class Ipv4Field(Field):
    field_type: IPv4Address = IPv4Address
