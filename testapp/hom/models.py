from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField()
    price=models.IntegerField()
    user=models.ForeignKey( User,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user=models.ForeignKey( User,models.SET_NULL,blank=True,null=True)
    course=models.ForeignKey(Course,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.course.name