import attr
from ndk.definitions import hostgroup


@attr.s
class HostGroup(hostgroup.HostGroupDirective):
    alias = attr.ib(type=str,
                    converter=str,
                    validator=attr.validators.instance_of(str),
                    kw_only=True)

    @alias.default
    def _set_alias_as_hostgroup_name(self):
        return self.hostgroup_name
