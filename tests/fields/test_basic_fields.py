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


class StringFieldTestCase(unittest.TestCase):

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


class IntegerFieldTestCase(unittest.TestCase):

    def test_IntegerField_is_works(self):
        f = fields.IntegerField()
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_type_conversion_of_default_in_IntegerField(self):
        with self.assertRaises(ValueError):
            fields.IntegerField(default='foo')

        f = fields.IntegerField(default='1234')
        assert isinstance(f.default, int)
        assert 1234 == f.default

        f = fields.IntegerField(default=1234)
        assert isinstance(f.default, int)
        assert 1234 == f.default


class BooleanFieldTestCase(unittest.TestCase):

    def test_BooleanField_is_works(self):
        f = fields.BooleanField()
        assert f.primary_key == False
        assert f.requried == False
        assert f.composite_key == False
        assert f.default == None

    def test_type_conversion_of_default_in_BooleanField(self):
        # Nagios Object use [0/1] to represent the Boolean value
        f = fields.BooleanField(default=True)
        assert isinstance(f.default, int)

        f = fields.BooleanField(default=True)
        assert f.default

        f = fields.BooleanField(default=0)
        assert not f.default
