from ndk import fields, core


class ContactGroupConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::ContactGroup
    """

    class Meta:
        object_type = 'contactgroup'

    contactgroup_name = fields.StringField(primary_key=True, requried=True)
    alias = fields.StringField(requried=True)
    members = fields.ForeignKey(relation='Contact')
    contactgroup_members = fields.ForeignKey(relation='ContactGroup')

    def __init__(self, stack, contactgroup_name, alias,
                 members=None, contactgroup_members=None):
        super().__init__(stack=stack, contactgroup_name=contactgroup_name,
                         alias=alias, members=members,
                         contactgroup_members=contactgroup_members)


class ContactGroup(ContactGroupConstruct):
    """
    L2 Construct: Nagios::Object::ContactGroup
    """

    def __init__(self, stack, contactgroup_name, alias=None, **kwargs):
        alias = alias or contactgroup_name
        super().__init__(stack, contactgroup_name, alias, **kwargs)


class MIS(ContactGroup):
    """
    L3 Construct: Nagios::Object::ContactGroup
    """

    contactgroup_name = fields.StringField(
        primary_key=True, requried=True, default='MIS')
    alias = fields.StringField(requried=True, default='MIS')

    def __init__(self, stack, members=None, contactgroup_members=None,
                 **kwargs):
        super().__init__(stack, members=members,
                         contactgroup_members=contactgroup_members,
                         **kwargs)
