import unittest

from ndk.definitions import HostGroupDirective
from ndk.stack import Stack


class HostGroupDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('HostGroupTesting')

    def test_contact_group_directive(self):
        HostGroupDirective(
            self.stack, hostgroup_name='foo', alias='bar')

    def test_hostgroup_members(self):
        cg_foo = HostGroupDirective(
            self.stack, hostgroup_name='foo', alias='FOO')
        cg_bar = HostGroupDirective(
            self.stack, hostgroup_name='bar', alias='BAR')
        contact = HostGroupDirective(
            self.stack, hostgroup_name='for-bar', alias='Foo Bar',
            hostgroup_members=[cg_foo, cg_bar])
        assert 'hostgroup_members    foo,bar' in contact.synth()
