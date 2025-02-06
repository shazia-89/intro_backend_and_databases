from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetail(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

