import asyncio
from django.http import HttpResponse
from django.views import View
from .models import Client
import json
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async



class Register(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        if 'username' not in body or 'password' not in body or body['username'] == '' or body['password'] == '':
            return HttpResponse('Incorrect Body')
        try:
            user_obj = User.objects.create_user(username=body['username'], email='',
                                                    password=body['password'])
            Client.objects.create(name=body['username'], user=user_obj)
        except Exception as e:
            print("Error while calling the register API : %s"%e)
            return HttpResponse('Something is wrong ! Please try again later')
        return HttpResponse('User Successfully Registerd !')
