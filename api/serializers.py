from django.contrib.auth.models import User

from rest_framework import serializers

from explorer.models import Polity

class PolitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Polity
        fields = ('id', 'name', 'web_site', 'election_website', 'next_election',
                  'num_representatives', 'num_wards', 'separate_executive',
                  'notes', 'creator')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # polities = serializers.PrimaryKeyRelatedField(many=True,
    #                                               queryset=Polity.objects.all())
    polities = serializers.HyperlinkedRelatedField(
        many=True, view_name='polity-detail', read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'polities')
