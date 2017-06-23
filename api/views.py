from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from explorer.models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *


# API Call:  http://127.0.0.1:8000/api/polities/1.json


class PolityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions
    """
    queryset = Polity.objects.all()
    serializer_class = PolitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides 'list' and 'detail' views
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'polities': reverse('polity-list', request=request, format=format)
    })


#
# class PolityList(generics.ListCreateAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PolityDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PolityList(APIView):
#     """
#     List all polities or create a new polity
#     """
#     def get(self, request, format=None):
#         polities = Polity.objects.all()
#         serializer = PolitySerializer(polities, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PolitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PolityDetail(APIView):
#     """
#     Retrieve, update or remove a polity
#     """
#     def get_object(self, pk):
#         try:
#             return Polity.objects.get(pk=pk)
#         except Polity.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         polity = self.get_object(pk)
#         serializer = PolitySerializer(polity)
#         return Response(serializer.data)
#
#     def put(self, request, pk, fomat=None):
#         polity = self.get_object(pk)
#         serializer = PolitySerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object.pk
#         snippet.delete()
#         return Response(statsu-status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def polity_list(request, format=None):
#     """
#     Test code to work see Django REST implementation
#     """
#     if request.method == 'GET':
#         polity = Polity.objects.all()
#         serializer = PolitySerializer(polity, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PolitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def polity_detail(request, pk, format=None):
#     """
#     Test code for Django REST implementation
#     """
#     try:
#         polity = Polity.objects.get(pk=pk)
#     except Polity.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PolitySerializer(polity)
#         return Response(polity.data)
#     elif request.method == 'PUT':
#         serializer = PolitySerializer(polity, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         polity.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
