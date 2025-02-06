from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentDetail(APIView):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

