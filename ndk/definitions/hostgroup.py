import attr
from ndk.construct import Construct
from ndk.directives import *


@attr.s
class HostGroupDirective(Construct):
    __object_type__ = 'hostgroup'

    hostgroup_name = PrimaryKey()
    alias = StringField(required=True)
    members = OneToMany('Host')
    hostgroup_members = OneToMany('HostGroup')
    notes = StringField()
    notes_url = StringField()
    action_url = StringField()

    @property
    def pk(self):
        return self.hostgroup_name
