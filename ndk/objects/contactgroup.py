from ndk import core, fields


class ContactGroupConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::ContactGroup

    This construct correspond directly to object defined by Nagios.
    """

    class Meta:
        object_type = 'contactgroup'

    contactgroup_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField(required=True)
    members = fields.ForeignKey(relation='Contact')
    contactgroup_members = fields.ForeignKey(relation='ContactGroup')

    def __init__(
            self, stack, contactgroup_name, alias, members=None,
            contactgroup_members=None):
        super().__init__(
            stack=stack, contactgroup_name=contactgroup_name,
            alias=alias, members=members,
            contactgroup_members=contactgroup_members)


class ContactGroup(ContactGroupConstruct):
    """
    L2 Construct: Nagios::Object::ContactGroup

    L2 encapsulate L1 modules, it is developed to address specific use
    cases and sensible defaults.
    """

    def __init__(self, stack, contactgroup_name, alias=None, **kwargs):
        alias = alias or contactgroup_name
        super().__init__(stack, contactgroup_name, alias, **kwargs)
