import unittest

from ndk import core, objects
from ndk.objects import ServiceGroup, ServiceGroupConstruct


class ServiceGroupTestCase(unittest.TestCase):

    def test_L1_construct_is_works(self):
        stack = core.Stack('ServiceGroupTesting')
        cg = ServiceGroupConstruct(
            stack, servicegroup_name='foo', alias='bar', members='baz')
        assert cg.servicegroup_name == 'foo'

    def test_L2_construct_is_works(self):
        stack = core.Stack('ServiceGroupTesting')
        cg = ServiceGroup(stack, servicegroup_name='foo',
                          alias='bar', members=['bar', 'baz'])
        assert cg.members == ['bar', 'baz']
