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
    creator = models.ForeignKey('auth.User', related_name='polities',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)


class Election(models.Model):
    """
    Election details
    """
    polity = models.ForeignKey(Polity,
                               on_delete=models.CASCADE)
    vote_date = models.DateField()
    start_date = models.DateField(null=True, blank=True)


class District(models.Model):
    """
    Information on ridings/wards/districts
    """
    polity = models.ForeignKey(Polity,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=25,
                              null=True, blank=True)
    num_reps = models.IntegerField(default=1,)
    is_whole_polity = models.BooleanField(default=False,)


class Politician(models.Model):
    """
    Information on individuals running for office
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    web_site = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)


class Candidate(models.Model):
    """
    Information on Candidates
    """
    politician = models.ForeignKey(Politician,
                                   on_delete=models.CASCADE)
    election = models.ForeignKey(Election,
                                 on_delete=models.CASCADE)
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE)
    incumbent = models.BooleanField(default=False)

    class Meta:
        unique_together = ('politician', 'election', 'district')


class Poll(models.Model):
    election = models.OneToOneField(Election)
    name = models.CharField(max_length=100, default='default')


class Question(models.Model):
    poll = models.ManyToManyField(Poll)
    question = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question)
    agreement = models.IntegerField(default=5)
    importance = models.IntegerField(default=5)


class CandidatePosition(Answer):
    candidate = models.ForeignKey(Candidate)


class PublicAnswer(Answer):
    ip_address = models.GenericIPAddressField()
