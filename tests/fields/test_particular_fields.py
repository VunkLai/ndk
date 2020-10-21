import ipaddress
import unittest
from enum import Enum

from ndk import exceptions, fields


class Ipv4FieldTestCase(unittest.TestCase):

    def test_Ipv4Field_is_works(self):
        f = fields.Ipv4Field()
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_type_conversion_of_default_in_Ipv4Field(self):
        with self.assertRaises(ipaddress.AddressValueError):
            fields.Ipv4Field(default='foo')

        f = fields.Ipv4Field(default='127.0.0.1')
        assert isinstance(f.default, ipaddress.IPv4Address)
        assert '127.0.0.1' == str(f.default)
        assert 2130706433 == int(f.default)


class EnumOptions(Enum):
    FOO = 'f'
    BAR = 'b'


class Options:
    FOOBAR = 'fb'


class ChoiceFieldTestCase(unittest.TestCase):

    def test_ChoiceField_is_works(self):
        # `.choices` is requried
        with self.assertRaises(exceptions.IntegrityError):
            fields.ChoiceField()

        with self.assertRaises(exceptions.IntegrityError):
            fields.ChoiceField(choices=Options)

        f = fields.ChoiceField(choices=EnumOptions)
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_type_conversion_of_default_in_ChoiceField(self):
        f = fields.ChoiceField(choices=EnumOptions,
                               default=EnumOptions.FOO)
        assert f.default == 'f'

        f = fields.ChoiceField(choices=EnumOptions,
                               default=[EnumOptions.FOO, EnumOptions.BAR])
        assert f.default == 'f,b'
