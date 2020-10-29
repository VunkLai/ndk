import attr
from ndk.definitions import servicegroup


@attr.s
class ServiceGroup(servicegroup.ServiceGroupDirective):
    alias = attr.ib(type=str,
                    converter=str,
                    validator=attr.validators.instance_of(str),
                    kw_only=True)

    @alias.default
    def _set_alias_as_servicegroup_name(self):
        return self.servicegroup_name
