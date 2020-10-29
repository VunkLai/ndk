
import attr
from ndk.definitions import contactgroup


@attr.s
class ContactGroup(contactgroup.ContactGroupDirective):
    alias = attr.ib(type=str,
                    converter=str,
                    validator=attr.validators.instance_of(str),
                    kw_only=True)

    @alias.default
    def _set_alias_as_contactgroup_name(self):
        return self.contactgroup_name
