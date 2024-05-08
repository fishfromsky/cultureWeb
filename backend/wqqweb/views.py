from .models import UserProfile
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .views_package.comment import comment_views
from .views_package.news import news_view
from .views_package.buy import buy_views
from .views_package.show import show_views


@require_http_methods(['POST'])
def login(request):
    response = {'code': 2000, 'message': 'success'}
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user_count = UserProfile.objects.filter(username=username).count()
    if user_count == 0:
        response['code'] = 1
        response['message'] = 'User not found'
        return JsonResponse(response)
    else:
        if not UserProfile.objects.filter(username=username, password=password).count():
            response['code'] = 2
            response['message'] = 'Password Wrong'
            return JsonResponse(response)
        else:
            user = UserProfile.objects.get(username=username, password=password)
            if Token.objects.filter(user=user):
                Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = str(token.key)
            user.save()
            data = {
                'username': username,
                'token': str(token.key),
                'roles': [user.role],
                'id': user.id
            }
            response['data'] = data
            response['code'] = 0
            return JsonResponse(response)


@require_http_methods(['POST'])
def register(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    username = data.get('name')
    password = data.get('password')
    user_count = UserProfile.objects.filter(username=username).filter().count()
    if user_count != 0:
        response['code'] = 1
        response['message'] = 'Username has already existed'
        return JsonResponse(response)
    else:
        user = UserProfile(username=username, password=password, email='', phone_number='', province='',
                           district='', address='')
        user.save()
        return JsonResponse(response)

