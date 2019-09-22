# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    """
    Client model to be utilized for populating the
    select list in the view.
    """
    name = models.CharField(max_length=64, default='', blank=False, null=False)
    contact = models.CharField(max_length=64, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Clients'


class Project(models.Model):
    """
    The Project model is to identify the software that the client
    is requesting the feature for.
    """
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Projects'


class FeatureRequest(models.Model):
    title = models.CharField(max_length=48, blank=False, null=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    project = models.ForeignKey(Project, related_name='requests', null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='requests', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['priority', 'project']
        ordering = ['project', 'priority']
        verbose_name = 'Feature Requests'
