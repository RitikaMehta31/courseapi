from rest_framework import serializers
from .models import Course,Wishlist

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Course
		fields=['id','name','author','date','price']

class WishlistSerializer(serializers.ModelSerializer):

	course = CourseSerializer(many=False)

	class Meta:
		model=Wishlist
		fields= ['id','course']