from rest_framework import serializers
from item.models import Course,Fun,Merchant
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
UserModel=get_user_model()
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
    #course = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    #merchant = serializers.PrimaryKeyRelatedField(many=True, queryset=Merchant.objects.all())
    password = serializers.CharField(write_only=True)
    #fun = serializers.PrimaryKeyRelatedField(many=True, queryset=Fun.objects.all())
    def create(self, validated_data):
        user = UserModel.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = UserModel
        fields = ('id', 'username','password',)#'course','merchant','fun',)
