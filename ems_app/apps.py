from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class EmsAppConfig(AppConfig):
    name = 'ems_app'
    verbose_name = _("List of Items")
