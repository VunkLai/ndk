from ndk import core, fields


class ServiceGroupConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::ServiceGroup
    """

    class Meta:
        object_type = 'servicegroup'

    servicegroup_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField(required=True)
    members = fields.ForeignKey(relation='Service')
    servicegroup_members = fields.ForeignKey(relation='ServiceGroup')
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()

    def __init__(
            self, stack, servicegroup_name, alias, members=None,
            servicegroup_members=None, notes=None, notes_url=None,
            action_url=None):
        super().__init__(
            stack, servicegroup_name=servicegroup_name, alias=alias,
            members=members, servicegroup_members=servicegroup_members,
            notes=notes, notes_url=notes_url, action_url=action_url)


class ServiceGroup(ServiceGroupConstruct):
    """
    L2 Construct: Nagios::Object::ServiceGroup
    """

    def __init__(self, stack, servicegroup_name, alias=None, **kwargs):
        alias = alias or servicegroup_name
        super().__init__(
            stack, servicegroup_name=servicegroup_name, alias=alias, **kwargs)
