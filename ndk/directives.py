import typing
from importlib import import_module

from attr import converters
from attr import ib as field
from attr import validators


class Converters:
    STR = converters.optional(str)
    INT = converters.optional(int)
    BOOL = converters.optional(bool)

    @staticmethod
    def PrimaryKey(name):
        return str(name).lower().replace(' ', '-')


def PrimaryKey():
    return field(type=str, converter=Converters.PrimaryKey)


def StringField(required=False):
    if required:
        return field(type=str, converter=str, kw_only=True)
    return field(
        type=str, converter=Converters.STR, default=None, kw_only=True)


def IntegerField(required=False):
    if required:
        return field(type=int, converter=int, kw_only=True)
    return field(
        type=int, converter=Converters.INT, default=None, kw_only=True)


def BooleanField(required=False):
    if required:
        return field(type=bool, converter=bool, kw_only=True)
    return field(
        type=bool, converter=Converters.BOOL, default=None, kw_only=True)


def ForeignKey(relation, required=False):
    module = import_module(f'ndk.definitions.{relation.lower()}')
    cls = getattr(module, relation+'Directive')
    if required:
        return field(
            type=cls,
            validator=validators.instance_of(cls),
            kw_only=True)
    return field(
        type=cls,
        validator=validators.optional(validators.instance_of(cls)),
        default=None,
        kw_only=True)


def ChoiceField(items, required=False):
    if required:
        return field(
            type=typing.List[items],
            validator=validators.deep_iterable(
                member_validator=validators.instance_of(items),
                iterable_validator=validators.instance_of(list))
        )
    else:
        return field(
            type=items,
            validator=validators.optional(
                validators.deep_iterable(
                    member_validator=validators.instance_of(items),
                    iterable_validator=validators.instance_of(list))
            ),
            default=None,
            kw_only=True)
