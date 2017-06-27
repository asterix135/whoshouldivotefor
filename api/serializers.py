from django.contrib.auth.models import User

from rest_framework import serializers

from explorer.models import *

class SimplePolitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity
        fields = ('id', 'name')


class SimpleDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'num_reps', 'is_whole_polity',
                  'shapefile_link')


class SimpleCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'web_site',
                  'twitter_handle', 'email', 'phone')


class SimpleIssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ('id', 'category',)


class ElectionSerializer(serializers.ModelSerializer):
    polity = SimplePolitySerializer()

    class Meta:
        model = Election
        fields = ('id', 'polity', 'vote_date', 'campaign_start_date')


class SimplePollSerializer(serializers.ModelSerializer):
    election = ElectionSerializer()

    class Meta:
        model = Poll
        fields = ('id', 'name', 'election')


class SimpleQuestionSerializer(serializers.ModelSerializer):
    poll = SimplePollSerializer()

    class Meta:
        model = Question
        fields = ('id', 'question', 'poll')


class QuestionSerializer(serializers.ModelSerializer):
    poll = SimplePollSerializer()
    category = SimpleIssueCategorySerializer(many=True,
                                             read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'category', 'poll')


class IssueCategorySerializer(serializers.ModelSerializer):
    category_questions = SimpleQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = IssueCategory
        fields = ('id', 'category', 'category_questions')


class DistrictSerializer(serializers.ModelSerializer):
    polity = SimplePolitySerializer()

    class Meta:
        model = District
        fields = ('id', 'name', 'number', 'polity', 'num_reps',
                  'is_whole_polity', 'shapefile_link', )


class SimpleElectionCandidateSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    election = ElectionSerializer(read_only=True)

    class Meta:
        model = ElectionCandidate
        fields = ('id', 'election', 'district', 'incumbent')


class SimpleCandidatePositionSerializer(serializers.ModelSerializer):
    question = SimpleQuestionSerializer()

    class Meta:
        model = CandidatePosition
        fields = ('id', 'question', 'agreement', 'importance')


class PolitySerializer(serializers.ModelSerializer):
    parent_polity = SimplePolitySerializer()
    districts = SimpleDistrictSerializer(many=True,
                                         read_only=True)

    class Meta:
        model = Polity
        fields = ('id', 'name', 'web_site', 'election_website', 'next_election',
                  'num_representatives', 'num_wards', 'separate_executive',
                  'notes', 'parent_polity', 'districts')


class PollSerializer(serializers.ModelSerializer):
    election = ElectionSerializer()

    class Meta:
        model = Poll
        fields = ('id', 'name', 'election')


class ElectionCandidateSerializer(serializers.ModelSerializer):
    candidate = SimpleCandidateSerializer(read_only=True)
    election = ElectionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = ElectionCandidate
        fields = ('id', 'candidate', 'incumbent', 'election', 'district')


class CandidateSerializer(serializers.ModelSerializer):
    candidate_in = SimpleElectionCandidateSerializer(many=True,
                                                     read_only=True)
    positions = SimpleCandidatePositionSerializer(many=True,
                                                  read_only=True)

    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'web_site',
                  'twitter_handle', 'email', 'phone', 'candidate_in',
                  'positions')


class CandidatePositionSerializer(serializers.ModelSerializer):
    candidate = ElectionCandidateSerializer()
    # candidate = serializers.StringRelatedField()
    question = SimpleQuestionSerializer()

    class Meta:
        model = CandidatePosition
        fields = ('id',
                  'candidate',
                  'question', 'agreement', 'importance')


class PublicAnswerSerializer(serializers.ModelSerializer):
    question = SimpleQuestionSerializer()

    class Meta:
        model = PublicAnswer
        fields = ('id', 'question', 'agreement', 'importance')
