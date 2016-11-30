from item.models import Course,Merchant,Fun
from item.serializers import CourseSerializer,MerchantSerializer,FunSerializer,UserSerializer
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from item.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model


class CourseList(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MerchantList(generics.ListCreateAPIView):
    queryset=Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FunList(generics.ListCreateAPIView):
    queryset=Fun.objects.all()
    serializer_class = FunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class MerchantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Merchant.objects.all()
    serializer_class=MerchantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class FunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Fun.objects.all()
    serializer_class=FunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    model = get_user_model()
    queryset=User.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
