from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProfileSerializerList, ProfileSerializerOne, ProfileSerializerPut
from .models import Profile


class ProfileList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializerList(profiles, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileOne(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        profile = Profile.objects.get(id=id)
        serializer = ProfileSerializerOne(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        profile = self.get_object(id)
        serializer = ProfileSerializerPut(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

