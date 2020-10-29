import attr
from ndk.construct import Construct
from ndk.directives import *


@attr.s
class CommandDirective(Construct):
    __object_type__ = 'command'

    command_name = PrimaryKey()
    command_line = StringField(required=True)

    @property
    def pk(self):
        return self.command_name
