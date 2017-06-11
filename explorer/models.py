from django.db import models

from .constants import *


class Polity(models.Model):
    """
    contains information on political entities
    """
    name = models.CharField(max_length=255)
    polity_type = models.CharField(choices=POLITY_TYPES,
                                   default='City',
                                   max_length=50)
    parent_polity = models.ForeignKey('self', on_delete=models.CASCADE,
                                      null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)
    election_website = models.URLField(null=True, blank=True)
    next_election = models.DateField(null=True, blank=True)
    num_representatives = models.IntegerField(null=True, blank=True)
    num_wards = models.IntegerField(null=True, blank=True)
    separate_executive = models.BooleanField(default=True)  # usually refers to mayor
    notes = models.TextField(null=True, blank=True)
    creator = models.ForeignKey('auth.User', related_name='polity',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)
