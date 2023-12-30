from django.contrib.auth.models import User
from .models import UserExtra
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
import json
import datetime

# Create your views here.
def getUsers(request):
    try:
        users = User.objects.select_related('userextra').values(
            'id', 'username', 'first_name', 'last_name', 'email', 'userextra__birthdate')
    except Exception as e:
        pass

    users = [
        {
            'id': user['id'],
            'username': user['username'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'birthdate': str(user['userextra__birthdate'])
        } for user in users
    ]

    return JsonResponse(users, safe = False)

def getUser(request, user_id):

    try:
        user = User.objects.get(pk=user_id)
        user_extra = UserExtra.objects.get(pk=user_id)
    except User.DoesNotExist and UserExtra.DoesNotExist:
        return JsonResponse({
            "error":"Some weird shit happened"
        })
    
    return JsonResponse({
        "id": user.id,
        "fullname": user.get_full_name(),
        "birthdate": user_extra.birthdate,
        "username": user.get_username(),
        "email": user.email
    })

def createUser(request):

    if request.method != "POST":
        return HttpResponseBadRequest

    data = request.POST

    user, _ = User.objects.get_or_create(
        username=data['username'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
    )

    user = User.objects.get(pk=user.id)

    user_extra, _ = UserExtra.objects.get_or_create(
        user=user,
        birthdate=data['birthdate']
    )

    return JsonResponse({
        "id": user.id,
        "fullname": user.get_full_name(),
        "birthdate": user_extra.birthdate,
        "username": user.get_username(),
        "email": user.email,
    })