from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'name', 'url_video', 'description', 'created_at', 'subcriptors')