import unittest

from ndk import core, exceptions, fields, objects


class ForeignKeyTestCase(unittest.TestCase):

    def test_foreign_key_is_works(self):
        class Host(core.Object):
            class Meta:
                object_type = 'host'
            host_name = fields.StringField(primary_key=True)
            parents = fields.ForeignKey(relation='Host')

        stack = core.Stack('ForeignKeyTesting')
        Host(stack, host_name='foo', parents='bar')
