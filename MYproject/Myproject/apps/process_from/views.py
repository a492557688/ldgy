from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import View
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
# Create your views here.
from Myproject.settings import  dev
class Submit_fwtg(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        user=request.data.get("name")
        phone=request.data.get("phone")
        jiedao=request.data.get("jiedao")
        data1=request.data.get("data1")
        beizhu=request.data.get("beizhu")
        msg=f"用户:{user}手机号:{phone}需要您处理,客户预约时间为{data1},备注信息:{beizhu},请尽快联系！"
        print(msg)
        from django.core.mail import send_mail
        send_mail("您收到一份需要处理房屋托管的邮件",msg,dev.EMAIL_HOST_USER,[dev.DEFAULT_FROM_EMAIL])

        return Response("已发送")
