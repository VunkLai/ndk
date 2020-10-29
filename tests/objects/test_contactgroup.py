import unittest

from ndk.objects import ContactGroup
from ndk.stack import Stack


class ContactGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ContactGroupTesting')

    def test_contact_group(self):
        cg = ContactGroup(self.stack, contactgroup_name='Foo')
        assert cg.pk == 'foo'
        assert cg.alias == 'foo'

    def test_alias(self):
        cg = ContactGroup(self.stack, contactgroup_name='foo', alias='bar')
        assert cg.contactgroup_name == 'foo'
        assert cg.alias == 'bar'
