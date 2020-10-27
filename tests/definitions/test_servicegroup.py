import unittest

from ndk.definitions import ServiceGroupDirective
from ndk.stack import Stack


class ServiceGroupDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ServiceGroupTesting')

    def test_contact_group_directive(self):
        ServiceGroupDirective(
            self.stack, servicegroup_name='foo', alias='bar')

    def test_servicegroup_members(self):
        cg_foo = ServiceGroupDirective(
            self.stack, servicegroup_name='foo', alias='FOO')
        cg_bar = ServiceGroupDirective(
            self.stack, servicegroup_name='bar', alias='BAR')
        contact = ServiceGroupDirective(
            self.stack, servicegroup_name='for-bar', alias='Foo Bar',
            servicegroup_members=[cg_foo, cg_bar])
        assert 'servicegroup_members    foo,bar' in contact.synth()
