import attr
from ndk.construct import Construct
from ndk.directives import *


@attr.s
class ContactGroupDirective(Construct):
    __object_type__ = 'contactgroup'

    contactgroup_name = PrimaryKey()

    @property
    def pk(self):
        return self.contactgroup_name
