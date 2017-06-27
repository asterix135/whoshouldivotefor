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

    def __str__(self):
        return str({'pk': self.pk, 'name': self.name})


class Election(models.Model):
    """
    Election details
    """
    polity = models.ForeignKey(Polity,
                               on_delete=models.CASCADE)
    vote_date = models.DateField()
    campaign_start_date = models.DateField(null=True, blank=True)


class District(models.Model):
    """
    Information on ridings/wards/districts
    """
    polity = models.ForeignKey(Polity,
                               related_name='districts',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=25,
                              null=True, blank=True)
    num_reps = models.IntegerField(default=1,)
    is_whole_polity = models.BooleanField(default=False,)
    shapefile_link = models.URLField(null=True, blank=True)


class Candidate(models.Model):
    """
    Information on individuals running for office
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    web_site = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ElectionCandidate(models.Model):
    """
    Information on Candidates particular to a specific election
    """
    candidate = models.ForeignKey(Candidate,
                                   on_delete=models.CASCADE,
                                   related_name='candidate_in')
    election = models.ForeignKey(Election,
                                 on_delete=models.CASCADE,
                                 related_name='candidate_details')
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE)
    incumbent = models.BooleanField(default=False)

    class Meta:
        unique_together = ('candidate', 'election', 'district')


class Poll(models.Model):
    """
    Selection of questions for a particular election
    """
    election = models.ForeignKey(Election,
                                 on_delete=models.CASCADE,
                                 related_name='polls')
    name = models.CharField(max_length=100, default='default')


class IssueCategory(models.Model):
    """
    Provides broader categories for poll questions
    """
    category = models.CharField(max_length=100,
                                unique=True)

class Question(models.Model):
    """
    Questions are designed to be of the form (agree/disagree) on a scale
    So, no answer choices are created
    """
    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE,
                             related_name='questions')
    category = models.ManyToManyField(IssueCategory,
                                      related_name='category_questions')
    question = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    agreement = models.IntegerField(default=5)
    importance = models.IntegerField(default=5)


class CandidatePosition(Answer):
    candidate = models.ForeignKey(ElectionCandidate,
                                  on_delete=models.CASCADE,
                                  related_name='positions')


class PublicAnswer(Answer):
    ip_address = models.GenericIPAddressField()
    session_id = models.CharField(max_length=255)
