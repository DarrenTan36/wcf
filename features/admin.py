# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from features.models import Client, FeatureRequest, Project

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(FeatureRequest)
