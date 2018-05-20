# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'apps.person'

    def ready(self):
        import apps.person.signals
