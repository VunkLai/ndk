import unittest

from ndk.definitions import ContactGroupDirective
from ndk.stack import Stack


class ContactGroupDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ContactGroupTesting')

    def test_contact_group_directive(self):
        ContactGroupDirective(
            self.stack, contactgroup_name='foo', alias='bar')

    def test_contactgroup_members(self):
        cg_foo = ContactGroupDirective(
            self.stack, contactgroup_name='foo', alias='FOO')
        cg_bar = ContactGroupDirective(
            self.stack, contactgroup_name='bar', alias='BAR')
        contact = ContactGroupDirective(
            self.stack, contactgroup_name='for-bar', alias='Foo Bar',
            contactgroup_members=[cg_foo, cg_bar])
        assert 'contactgroup_members    foo,bar' in contact.synth()
