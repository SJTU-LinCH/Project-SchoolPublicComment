from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Course(models.Model):
    coursename = models.CharField(max_length=20)
    score = models.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(100)])
    def __unicode__(self):
        return self.coursename

class CourseAdmin(admin.ModelAdmin):
    list_display = ['coursename','score']
    
admin.site.register(Course,CourseAdmin)
