import attr
from ndk.construct import Construct
from ndk.directives import *
from ndk.options import service as options


@attr.s
class ServiceDirective(Construct):
    __object_type__ = 'service'

    host_name = PrimaryKey()
    hostgroup_name = OneToOne('HostGroup')
    service_description = PrimaryKey()
    display_name = StringField()
    parents = OneToMany('Service')
    importance = IntegerField()
    servicegroups = OneToMany('ServiceGroup')
    is_volatile = BooleanField()
    check_command = OneToOne('Command', required=True)
    initial_state = ChoiceField(options.InitialState)
    max_check_attempts = IntegerField(required=True)
    check_interval = IntegerField(required=True)
    retry_interval = IntegerField(required=True)
    active_checks_enabled = BooleanField()
    passive_checks_enabled = BooleanField()
    check_period = OneToOne('TimePeriod', required=True)
    obsess_over_service = BooleanField()
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
    notification_interval = IntegerField(required=True)
    first_notification_delay = IntegerField()
    notification_period = OneToOne('TimePeriod', required=True)
    notification_options = ChoiceField(options.Notification)
    notifications_enabled = BooleanField()
    contacts = OneToMany('Contact')
    contact_groups = OneToMany('ContactGroup')
    stalking_options = ChoiceField(options.Stalking)
    notes = StringField()
    notes_url = StringField()
    action_url = StringField()
    icon_image = StringField()
    icon_image_alt = StringField()

    @property
    def pk(self):
        return f'{self.host_name}::{self.service_description}'
