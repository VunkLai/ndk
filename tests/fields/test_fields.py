import ipaddress
import unittest

from ndk import fields


class FieldTestCase(unittest.TestCase):

    def test_Field_is_works(self):
        f = fields.Field()
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_normalize_name_is_works(self):
        assert 'foo-bar' == fields.Field.normalize_name('Foo BAR')

    def test_type_conversion_of_default(self):
        str_default = fields.Field(default='foo')
        assert isinstance(str_default.default, str)

        int_defualt = fields.Field(default=1234)
        assert isinstance(int_defualt.default, int)


class StringField(unittest.TestCase):

    def test_StringField_is_works(self):
        f = fields.StringField()
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_type_conversion_of_default_in_StringField(self):
        str_default = fields.StringField(default='foo')
        assert isinstance(str_default.default, str)

        int_default = fields.StringField(default=1234)
        assert isinstance(int_default.default, str)
        assert '1234' == int_default.default


class Ipv4Field(unittest.TestCase):

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
