from django.db import models

class Polity(models.Model):
    """
    contains information on political entities
    """
    name = models.CharField(max_length=255)
    parent_polity = models.ForeignKey('self', on_delete=models.CASCADE)
    web_site = models.URLField()
    election_website = models.URLField()
    next_election = models.DateField()
    num_representatives = models.IntegerField()
    num_wards = models.IntegerField()
    separate_executive = models.BooleanField()  # usually refers to mayor
    notes = models.TextField()
