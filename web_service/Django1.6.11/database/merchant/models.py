from django.db import models
from django.contrib import admin
# Create your models here.
class Merchant(models.Model):
    merchantname = models.CharField(max_length=20)
    merchantaddress= models.CharField(max_length=20)
    star = models.IntegerField()
    def __unicode__(self):
        return self. merchantname

class MerchantAdmin(admin.ModelAdmin):
    list_display = ['merchantname','merchantaddress','star']
    
admin.site.register(Merchant,MerchantAdmin)
