from rest_framework import serializers
from .models import teacher
from .models import student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =student
        fields = '__all__'