import unittest

from ndk import core, objects
from ndk.objects import HostGroup, HostGroupConstruct


class HostGroupTestCase(unittest.TestCase):

    def test_L1_construct_is_works(self):
        stack = core.Stack('HostGroupTesting')
        cg = HostGroupConstruct(
            stack, hostgroup_name='foo', alias='bar', members='baz')
        assert cg.hostgroup_name == 'foo'

    def test_L2_construct_is_works(self):
        stack = core.Stack('HostGroupTesting')
        cg = HostGroup(stack, hostgroup_name='foo',
                       alias='bar', members=['bar', 'baz'])
        assert cg.members == ['bar', 'baz']
