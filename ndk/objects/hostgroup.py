from ndk import core, fields


class HostGroupConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::HostGroup
    """

    class Meta:
        object_type = 'hostgroup'

    hostgroup_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField(required=True)
    members = fields.ForeignKey(relation='Host')
    hostgroup_members = fields.ForeignKey(relation='HostGroup')
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()

    def __init__(self, stack, hostgroup_name, alias, members=None,
                 hostgroup_members=None, notes=None, notes_url=None,
                 action_url=None):
        super().__init__(stack, hostgroup_name=hostgroup_name, alias=alias,
                         members=members, hostgroup_members=hostgroup_members,
                         notes=notes, notes_url=notes_url, action_url=action_url)


class HostGroup(HostGroupConstruct):
    """
    L2 Construct: Nagios::Object::HostGroup
    """

    def __init__(self, stack, hostgroup_name, alias, **kwargs):
        alias = alias or hostgroup_name
        super().__init__(
            stack, hostgroup_name=hostgroup_name, alias=alias, **kwargs)
