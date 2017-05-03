from django.db import models
from django.contrib import admin
# Create your models here.
class Entertainment(models.Model):
    entertainmentname = models.CharField(max_length=20)
    entertainmentaddress= models.CharField(max_length=30)
    service = models.CharField(max_length=200)
    def __unicode__(self):
        return self.  entertainmentname

class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['entertainmentname','entertainmentaddress','service']
    
admin.site.register(Entertainment,EntertainmentAdmin)
