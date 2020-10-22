import unittest

from ndk import core, objects
from ndk.objects import ContactGroup, ContactGroupConstruct


class ContactGroupTestCase(unittest.TestCase):

    def test_L1_constructs_are_works(self):
        stack = core.Stack('ContactGroupTesting')
        cg = ContactGroupConstruct(
            stack, contactgroup_name='foo', alias='bar', members='baz')
        assert cg.contactgroup_name == 'foo'

    def test_L2_constructs_are_works(self):
        stack = core.Stack('ContactGroupTesting')
        cg = ContactGroup(stack, contactgroup_name='foo',
                          alias='bar', members=['bar', 'baz'])
        assert cg.members == ['bar', 'baz']
