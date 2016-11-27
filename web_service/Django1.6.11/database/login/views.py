#coding=utf-8
#from django.shortcuts import render,render_to_response
#from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
#from django import forms
from login.models import User
from rest_framework import viewsets,generics,status,permissions
from login.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#这个跟django的类方法可不一样 以前都是self，现在是一个viewsets.ModelViewSet 类方法
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #查询用户信息models.User.objects.all().order_by('-date_joined')
    #UserSerializer 序列化(表现层，将数据按照一定格式来处理然后返回给前端)
    def list(self, request):
        #queryset，serializer_class 这个变量名是死的不能改
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
#表单
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(),max_length=20)
    userid = forms.IntegerField(label='用户ID')
#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #密码长度最少为6位
            if (len(password)<=5):
                return HttpResponse('regist failed!  Password should be no less than 6 characters!')
            #密码不能为纯数字
            count=0
            for i in range(len(password)): 
                if ('0'<=password[i]<='9'):
                    count+=1;
            if (count==len(password)):
                return HttpResponse('regist failed!  Password form illegitimate!  密码格式如下：1、不能少于6位字符，不能多于20位字符；2、不能仅含数字。')
            #比较用户名是否已经注册
            user = User.objects.filter(username__exact = username)
            if user:
                #比较失败，还在regist
                return HttpResponse('regist failed!  Username has existed!')
            else:
                #比较成功，跳转
                 #添加到数据库
                User.objects.create(username= username,password=password)
                return HttpResponse('regist success!!')
                
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/login/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
'''
