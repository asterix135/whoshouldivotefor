from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from explorer.models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *


# API Call:  http://127.0.0.1:8000/api/polities/1.json


class DistrictViewSet(viewsets.ModelViewSet):
    """
    Information on electoral districts for a specific Polity
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class PolityViewSet(viewsets.ModelViewSet):
    """
    Information on Governments with elected representatives in Canada
    """
    queryset = Polity.objects.all()
    serializer_class = PolitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]


class ElectionViewSet(viewsets.ModelViewSet):
    """
    Information on specific Elections
    """
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class ElectionCandidateViewSet(viewsets.ModelViewSet):
    """
    Information about who is runnining in a particular election & district
    """
    queryset = ElectionCandidate.objects.all()
    serializer_class = ElectionCandidateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class CandidateViewSet(viewsets.ModelViewSet):
    """
    General contact information on people running for office
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class IssueCategoryViewSet(viewsets.ModelViewSet):
    """
    Categories for Poll Questions
    """
    queryset = IssueCategory.objects.all()
    serializer_class = IssueCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class PollViewSet(viewsets.ModelViewSet):
    """
    Details on Polls associated with various elections
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class QuestionViewSet(viewsets.ModelViewSet):
    """
    Details on questions asked in various election polls
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    class Meta:
        ordering = ['id',]

class CandidatePositionViewSet(viewsets.ModelViewSet):
    """
    Details on positions taken by various political candidates
    """
    queryset = CandidatePosition.objects.all()
    serializer_class = CandidatePositionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

class PublicAnswerViewSet(viewsets.ModelViewSet):
    """
    Public Answers to various Poll Questions
    """
    queryset = PublicAnswer.objects.all()
    serializer_class = PublicAnswerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        ordering = ['id',]

@api_view(['GET'])
def api_root(request, format=None):
    """
    Directions on how to access API views
    """
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'polities': reverse('polity-list', request=request, format=format)
    })
