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
