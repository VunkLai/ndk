from ndk import fields, core


class NgsHostGroup(core.Object):
    """
    L1 Construct: Nagios::Object::HostGroup
    """

    class Meta:
        object_type = 'hostgroup'

    hostgroup_name = fields.StringField(primary_key=True, requried=True)
    alias = fields.StringField(requried=True)
    members = fields.ForeignKey('Host')
    hostgroup_members = fields.ForeignKey('HostGroup')
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()


class HostGroup(core.Object):
    """
    L2 Construct: Nagios::Object::HostGroup
    """

    def __init__(self, stack, hostgroup_name, alias, members=None, hostgroup_members=None, notes=None, notes_url=None, action_url=None):
        super().__init__(stack, hostgroup_name=hostgroup_name, alias=alias, members=members, hostgroup_members=hostgroup_members, notes=notes, notes_url=notes_url, action_url=action_url):
