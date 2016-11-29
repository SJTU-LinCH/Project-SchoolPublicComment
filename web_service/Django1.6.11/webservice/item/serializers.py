from rest_framework import serializers
from item.models import Course,Fun,Merchant
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Course
        fields = ('coursename','courseinfo', 'average', 'remarknum','owner' ,)
class MerchantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Merchant
        fields = ('merchantname','merchantinfo', 'average', 'remarknum','owner', )
class FunSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Fun
        fields = ('funname','funinfo', 'average', 'remarknum','owner', )

class UserSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    merchant = serializers.PrimaryKeyRelatedField(many=True, queryset=Merchant.objects.all())
    fun = serializers.PrimaryKeyRelatedField(many=True, queryset=Fun.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username','password','course','merchant','fun',)
