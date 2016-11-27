#coding=utf-8
#from django.shortcuts import render,render_to_response
#from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
#from django import forms
from merchant.models import Merchant
from rest_framework import viewsets,generics,status,permissions
from merchant.serializers import MerchantSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#这个跟django的类方法可不一样 以前都是self，现在是一个viewsets.ModelViewSet 类方法
class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    #查询用户信息models.User.objects.all().order_by('-date_joined')
    #UserSerializer 序列化(表现层，将数据按照一定格式来处理然后返回给前端)
    def list(self, request):
        #queryset，serializer_class 这个变量名是死的不能改
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Merchant.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MerchantSerializer(user)
        return Response(serializer.data)
    
class MerchantList(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantDetail(generics.RetrieveAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer



