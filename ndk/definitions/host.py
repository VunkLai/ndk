from ipaddress import IPv4Address

import attr
from ndk.construct import Construct
from ndk.directives import *
from ndk.options import host as options


@attr.s
class HostDirective(Construct):
    __object_type__ = 'host'

    host_name = PrimaryKey()
    alias = StringField(required=True)
    display_name = StringField()
    address = attr.ib(
        type=IPv4Address, converter=attr.converters.optional(IPv4Address),
        default=None, kw_only=True)
    parents = OneToMany('Host')
    importance = IntegerField()
    hostgroups = OneToMany('HostGroup')
    check_command = OneToOne('Command')
    initial_state = ChoiceField(options.InitialState)
    max_check_attempts = IntegerField(required=True)
    check_interval = IntegerField()
    retry_interval = IntegerField()
    active_checks_enabled = BooleanField()
    passive_checks_enabled = BooleanField()
    check_period = OneToOne('TimePeriod', required=True)
    obsess_over_host = BooleanField()
    check_freshness = BooleanField()
    freshness_threshold = IntegerField()
    event_handler = OneToOne('Command')
    event_handler_enabled = BooleanField()
    low_flap_threshold = IntegerField()
    high_flap_threshold = IntegerField()
    flap_detection_enabled = BooleanField()
    flap_detection_options = ChoiceField(options.FlapDetection)
    process_perf_data = BooleanField()
    retain_status_information = BooleanField()
    retain_nonstatus_information = BooleanField()
    contacts = OneToMany('Contact')
    contact_groups = OneToMany('ContactGroup')
    notification_interval = IntegerField(required=True)
    first_notification_delay = IntegerField()
    notification_period = OneToOne('TimePeriod', required=True)
    notification_options = ChoiceField(options.Notification)
    notifications_enabled = BooleanField()
    stalking_options = ChoiceField(options.Stalking)
    notes = StringField()
    notes_url = StringField()
    action_url = StringField()
    icon_image = StringField()
    icon_image_alt = StringField()
    vrml_image = StringField()
    statusmap_image = StringField()
    # _2d_coords = StringField()
    # _3d_coords = StringField()

    @property
    def pk(self):
        return self.host_name
