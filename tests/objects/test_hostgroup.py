import unittest

from ndk.objects import HostGroup
from ndk.stack import Stack


class HostGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('HostGroupTesting')

    def test_contact_group(self):
        cg = HostGroup(self.stack, hostgroup_name='Foo')
        assert cg.pk == 'foo'
        assert cg.alias == 'foo'

    def test_alias(self):
        cg = HostGroup(self.stack, hostgroup_name='foo', alias='bar')
        assert cg.hostgroup_name == 'foo'
        assert cg.alias == 'bar'
