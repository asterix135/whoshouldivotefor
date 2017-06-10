from rest_framework import serializers
from .models import Polity

class PolitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity
        fields = ('id', 'name', 'web_site', 'election_website', 'next_election',
                  'num_representatives', 'num_wards', 'separate_executive',
                  'notes')
