import unittest

# from . import models
from ndk import core, exceptions, fields


class NagiosTestCase(unittest.TestCase):

    def test_raise_IntegrityError_when_create_new_class(self):
        with self.assertRaises(exceptions.IntegrityError):
            class EmptyObject(core.Object):
                pass

        with self.assertRaises(exceptions.IntegrityError):
            class ObjectWithoutPK(core.Object):
                class Meta:
                    object_type = 'host'

                directive = fields.Field()

        with self.assertRaises(exceptions.IntegrityError):
            class ObjectWithoutObjectType(core.Object):

                directive = fields.Field(primary_key=True)

    def test_to_create_new_class(self):
        class GoodObject(core.Object):
            class Meta:
                object_type = 'host'
            host_name = fields.Field(primary_key=True)

        assert 'host' == GoodObject.__object_type__
        assert 'host_name' in GoodObject.__mappings__
        assert 'host_name' in GoodObject.__primary_key__
        assert not GoodObject.__composite_key__
        stack = core.Stack('ObjectTesting')
        host = GoodObject(stack, host_name='foo')

    def test_if_pk_has_certain_format(self):
        class ObjectWithOenPK(core.Object):
            class Meta:
                object_type = 'foo'
            host_name = fields.StringField(primary_key=True)

        class ObjectWithTwoPKs(core.Object):
            class Meta:
                object_type = 'foo'
            host_name = fields.StringField(primary_key=True)
            alias = fields.StringField(primary_key=True)

        stack = core.Stack('ObjectTesting')
        host = ObjectWithOenPK(stack, host_name='Foo Bar')
        assert host.pk == 'foo-bar'

        host = ObjectWithTwoPKs(stack, host_name='Foo Bar', alias='BAZ')
        assert host.pk == 'foo-bar::baz'

    def test_required_is_works_in_object(self):
        class Host(core.Object):
            class Meta:
                object_type = 'asdf'

            host_name = fields.StringField(required=True, primary_key=True)
            address = fields.Ipv4Field(required=True)

        stack = core.Stack('FieldTesting')
        with self.assertRaises(exceptions.IntegrityError):
            host = Host(stack, host_name='foo')
            host.is_valud()

        host = Host(stack, host_name='bar', address='127.0.0.1')
        host.is_valud()

        # host = Host(stack, host_name='foo')
        # assert host.host_name == 'foo'
