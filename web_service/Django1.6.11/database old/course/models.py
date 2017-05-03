from django.db import models
from django.contrib import admin
# Create your models here.
class Course(models.Model):
    coursename = models.CharField(max_length=20)
    average = models.FloatField(null=True, blank=True)
    population = models.IntegerField()
    
    def __unicode__(self):
        return self.coursename

class CourseAdmin(admin.ModelAdmin):
    list_display = ['coursename','average']
    
admin.site.register(Course,CourseAdmin)


