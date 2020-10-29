import unittest

from ndk.objects import ServiceGroup
from ndk.stack import Stack


class ServiceGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ServiceGroupTesting')

    def test_contact_group(self):
        cg = ServiceGroup(self.stack, servicegroup_name='Foo')
        assert cg.pk == 'foo'
        assert cg.alias == 'foo'

    def test_alias(self):
        cg = ServiceGroup(self.stack, servicegroup_name='foo', alias='bar')
        assert cg.servicegroup_name == 'foo'
        assert cg.alias == 'bar'
