import attr
from ndk.construct import Construct
from ndk.directives import *


@attr.s
class ServiceGroupDirective(Construct):
    __object_type__ = 'servicegroup'

    servicegroup_name = PrimaryKey()
    alias = StringField(required=True)
    members = OneToMany('Service')
    servicegroup_members = OneToMany('ServiceGroup')
    notes = StringField()
    notes_url = StringField()
    action_url = StringField()
 
    @property
    def pk(self):
        return self.servicegroup_name
