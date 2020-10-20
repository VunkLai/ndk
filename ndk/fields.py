from dataclasses import dataclass


@dataclass
class Field:
    primary_key: bool = False
    composite_key: bool = False
    requried: bool = False
    default: str = None

    @staticmethod
    def normalize_name(name):
        return str(name).lower().replace(' ', '-')
