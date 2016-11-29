from django.db import models

class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    coursename= models.CharField(max_length=100, default='')
    courseinfo=models.CharField(max_length=500,default='')
    average=models.FloatField(default=0)
    remarknum=models.IntegerField(default=0)
    owner=models.ForeignKey('auth.User',related_name='course')
    def __str__(self):
        return self.coursename + '(id:' + str(self.id) + ')'

class Merchant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    merchantname=models.CharField(max_length=100, default='')
    merchantinfo= models.CharField(max_length=500, default='')
    average=models.FloatField(default=0)
    remarknum=models.IntegerField(default=0)
    owner=models.ForeignKey('auth.User',related_name='merchant')
    def __str__(self):
        return self.merchantname + '(id:' + str(self.id) + ')'

class Fun(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    funname=models.CharField(max_length=100, default='')
    funinfo= models.CharField(max_length=500, default='')
    average=models.FloatField(default=0)
    remarknum=models.IntegerField(default=0)
    owner=models.ForeignKey('auth.User',related_name='fun')
    def __str__(self):
        return self.funname + '(id:' + str(self.id) + ')'
