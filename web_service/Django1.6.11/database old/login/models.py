from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __unicode__(self):
        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    
admin.site.register(User,UserAdmin)
