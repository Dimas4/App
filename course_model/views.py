from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CourseSerializerList, CourseSerializerOne
from .models import Course


class CourseList(APIView):
    def get(self, request, format=None):
        profiles = Course.objects.all()
        serializer = CourseSerializerList(profiles, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseOne(APIView):
    def get(self, request, id, format=None):
        profile = Course.objects.get(id=id)
        serializer = CourseSerializerOne(profile, context={'request': request})
        return Response(serializer.data)
