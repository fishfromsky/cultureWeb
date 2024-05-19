from .models import UserProfile
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .utils import to_dict
from .views_package.comment import comment_views
from .views_package.news import news_view
from .views_package.buy import buy_views
from .views_package.show import show_views
from .views_package.people import people_views


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


@require_http_methods(['POST'])
def info_modify(request):
    response = {'code': 20000, 'message': 'success'}
    data = json.loads(request.body)
    person_id = data.get('id')
    user = UserProfile.objects.get(id=person_id)
    if user.username != data.get('name'):
        user.username = data.get('name')
    if user.phone_number != data.get('mobile'):
        user.phone_number = data.get('mobile')
    if user.email != data.get('email'):
        user.email = data.get('email')
    if user.province != data.get('province'):
        user.province = data.get('province')
    if user.district != data.get('district'):
        user.district = data.get('district')
    if user.address != data.get('address'):
        user.address = data.get('address')
    if user.password != data.get('password'):
        user.password = data.get('password')
    user.save()
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_addresses(request):
    response = {'code': 0, 'message': 'success'}
    person_id = request.GET.get('id')
    person_dict = to_dict(UserProfile.objects.get(id=person_id))
    response['address'] = person_dict['address']
    response['province'] = person_dict['province']
    response['district'] = person_dict['district']
    response['post'] = person_dict['post_price']
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_username_info(request):
    response = {'code': 0, 'message': 'success'}
    person_id = request.GET.get('id')
    person_dict = to_dict(UserProfile.objects.get(id=person_id))
    response['data'] = person_dict
    return JsonResponse(response)

