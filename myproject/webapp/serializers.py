from rest_framework import serializers
from .models import teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =teacher
        fields = '__all__'