from ndk import fields, core


class NgsServiceGroup(core.Object):
    """
    L1 Construct: Nagios::Object::ServiceGroup
    """

    class Meta:
        object_type = 'servicegroup'

    servicegroup_name = fields.StringField(primary_key=True, requried=True)
    alias = fields.StringField(requried=True)
    members = fields.ForeignKey(relation='Service')
    servicegroup_members = fields.ForeignKey(relation='ServiceGroup')
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()


class ServiceGroup(NgsServiceGroup):
    """
    L2 Construct: Nagios::Object::ServiceGroup
    """

    def __init__(self, stack, servicegroup_name, alias, members=None, servicegroup_members=None, notes=None, notes_url=None, action_url=None):
        super().__init__(stack, servicegroup_name=servicegroup_name, alias=alias, members=members,
                         servicegroup_members=servicegroup_members, notes=notes, notes_url=notes_url, action_url=action_url)
