from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from rest_framework import permissions, generics
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from ..common.base_view import BaseView
from ..serializers import TokenSerializer
from .component.models import User
from .constants import ROLES

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def render_login_view(request, message=''):
    return render(request, 'logparser/auth/login.html', {'message': message})


@csrf_protect
def signup_func(request):
    if request.method == 'GET':
        return render(request, 'logparser/auth/signup.html', {})
    elif request.method == 'POST':
        return signup(request)


def signup(request):
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    
    user = User.objects.create_user(username=username, email=email, password=password)
    if user is not None: 
        user.role = ROLES.ROLE_USER
        user.save()
        return redirect('logparser:auth-login')
    return HttpResponseServerError()


@csrf_protect
def login_func(request, message=None):
    if request.method == 'GET':
        return render_login_view(request, message=message)
    elif request.method == 'POST':
        return post_login(request)


def post_login(request): 
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    
    if user is not None: 
        login(request, user)
        
        payload = jwt_payload_handler(user)
        payload.update({
            'role': user.role
        })

        token = jwt_encode_handler(payload)
        serializer = TokenSerializer(data={
            'token': token
        })

        serializer.is_valid()
        return redirect('logparser:dashboard')
    return render_login_view(request, message='Username or password is invalid')


def post_logout(request):
    logout(request)
    return redirect('logparser:auth-login')

