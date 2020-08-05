from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import teacher
from .serializers import TeacherSerializer

class teacherlist(APIView):
    def get(self,request):
        teacher1=teacher.objects.all()
        serializer=TeacherSerializer(teacher1,many=True)
        return Response(serializer.data)
    def post(self):
        pass