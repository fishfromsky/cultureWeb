from ...model_package.comment.comment_models import Comment, Liking, Guanzhu, Shoucang, Pinglun
from ...models import UserProfile
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from ...utils import to_dict
from collections import Counter


def return_com_dict(com, request_user):
    com_dict = to_dict(com)
    user_id = com_dict['user']
    com_id = com_dict['id']
    user = UserProfile.objects.get(id=user_id)
    comment_object = Comment.objects.get(id=com_id)

    com_dict['username'] = user.username
    com_dict['dianzan'] = Liking.objects.filter(comment=comment_object).count()
    request_user_dianzan = Liking.objects.filter(comment=comment_object, user=request_user).count()
    if request_user_dianzan:
        com_dict['my_dianzan'] = True
    else:
        com_dict['my_dianzan'] = False
    com_dict['pinglun'] = []
    pinglun_list = Pinglun.objects.filter(comment=Comment(id=com_id))
    for pinglun in pinglun_list:
        com_dict['pinglun'].append(to_dict(pinglun))
    guanzhu = Guanzhu.objects.filter(user=request_user, target_user=user).count()
    if guanzhu:
        com_dict['my_guanzhu'] = True
    else:
        com_dict['my_guanzhu'] = False
    shoucang = Shoucang.objects.filter(comment=comment_object, user=request_user).count()
    if shoucang:
        com_dict['shoucang'] = True
    else:
        com_dict['shoucang'] = False
    return com_dict

# 获取所有评论
@require_http_methods(['GET'])
def get_all_comments(request):
    response = {'code': 0, 'message': 'success'}
    request_user_id = request.GET.get('id')
    request_user = UserProfile.objects.get(id=request_user_id)
    comment_list = Comment.objects.all()
    response['data'] = []
    for com in comment_list:
        response['data'].append(return_com_dict(com, request_user))
    return JsonResponse(response)


# 添加关注列表
@require_http_methods(['POST'])
def add_guanzhu(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    target_user_id = data.get('target_user_id')
    user_id = data.get('user_id')
    guanzhu_object = Guanzhu.objects.create(user=UserProfile(id=user_id), target_user=UserProfile(id=target_user_id))
    guanzhu_object.save()
    return JsonResponse(response)


# 取消关注
@require_http_methods(['POST'])
def delete_guanzhu(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    target_user_id = data.get('target_user_id')
    user_id = data.get('user_id')
    guanzhu_object = Guanzhu.objects.get(user=UserProfile(id=user_id), target_user=UserProfile(id=target_user_id))
    guanzhu_object.delete()
    return JsonResponse(response)


# 添加点赞
@require_http_methods(['POST'])
def add_dianzan(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    comment_id = data.get('comment_id')
    user_id = data.get('user_id')
    liking_object = Liking.objects.create(comment=Comment(id=comment_id), user=UserProfile(id=user_id))
    liking_object.save()
    return JsonResponse(response)


# 取消点赞
@require_http_methods(['POST'])
def delete_dianzan(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    comment_id = data.get('comment_id')
    user_id = data.get('user_id')
    dianzan_object = Liking.objects.get(comment=Comment(id=comment_id), user=UserProfile(id=user_id))
    dianzan_object.delete()
    return JsonResponse(response)

# 添加收藏
@require_http_methods(['POST'])
def add_shoucang(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    comment_id = data.get('comment_id')
    user_id = data.get('user_id')
    shoucang_object = Shoucang.objects.create(comment=Comment(id=comment_id), user=UserProfile(id=user_id))
    shoucang_object.save()
    return JsonResponse(response)


# 取消收藏
@require_http_methods(['POST'])
def delete_shoucang(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    comment_id = data.get('comment_id')
    user_id = data.get('user_id')
    shoucang_object = Shoucang.objects.get(comment=Comment(id=comment_id), user=UserProfile(id=user_id))
    shoucang_object.delete()
    return JsonResponse(response)


# 获取用户个人被关注、收藏、点赞信息
@require_http_methods(['GET'])
def get_personal_info(request):
    response = {'code': 0, 'message': 'success'}
    user_id = request.GET.get('user_id')
    personal_data = {'dianzan': 0, 'guanzhu': 0, 'fensi': 0}
    personal_data['guanzhu'] = Guanzhu.objects.filter(user=UserProfile(id=user_id)).count()
    personal_data['fensi'] = Guanzhu.objects.filter(target_user=UserProfile(id=user_id)).count()
    personal_data['dianzan'] = Liking.objects.filter(comment__user=UserProfile(id=user_id)).count()
    response['data'] = personal_data
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_my_shoucang(request):
    response = {'code': 0, 'message': 'success'}
    user_id = request.GET.get('user_id')
    request_user = UserProfile(id=user_id)
    shoucang_objects = Shoucang.objects.filter(user=request_user)
    response['data'] = []
    for shoucang in shoucang_objects:
        response['data'].append(return_com_dict(shoucang.comment, request_user))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_my_guanzhu(request):
    response = {'code': 0, 'message': 'success'}
    user_id = request.GET.get('user_id')
    request_user = UserProfile(id=user_id)
    guanzhu_object = Guanzhu.objects.filter(user=request_user)
    response['data'] = []
    for user in guanzhu_object:
        comments = Comment.objects.filter(user=user.target_user)
        for com in comments:
            response['data'].append(return_com_dict(com, request_user))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_hot_comment(request):
    response = {'code': 0, 'message': 'success'}
    user_id = request.GET.get('user_id')
    request_user = UserProfile(id=user_id)
    hot_comment = Counter([like.comment for like in Liking.objects.all()])
    sorted_counter = sorted(hot_comment.items(), key=lambda x: x[1], reverse=True)
    response['data'] = []
    for com_tuple in sorted_counter:
        response['data'].append(return_com_dict(com_tuple[0], request_user))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_my_dianzan(request):
    response = {'code': 0, 'message': 'success'}
    user_id = request.GET.get('user_id')
    request_user = UserProfile(id=user_id)
    like_objects = Liking.objects.filter(user=request_user)
    response['data'] = []
    for like in like_objects:
        response['data'].append(return_com_dict(like.comment, request_user))
    return JsonResponse(response)


@require_http_methods(['POST'])
def get_search_content(request):
    response = {'code': 0, 'message': 'success'}
    data = json.loads(request.body)
    user_id = data.get('user_id')
    content = data.get('content')
    request_user = UserProfile(id=user_id)
    com_list = Comment.objects.filter(content__icontains=content)
    response['data'] = []
    for com in com_list:
        response['data'].append(return_com_dict(com, request_user))
    return JsonResponse(response)

