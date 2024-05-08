from django.views.decorators.http import require_http_methods
from ...model_package.show.show_models import Show_Ji, Show_Wen, Wen_Table, Wen_Comment, Material_Detail
from ...models import UserProfile
from ...utils import to_dict
from django.http import JsonResponse
import json


@require_http_methods(['GET'])
def get_ji_content(request):
    response = {'code': 0, 'message': 'success'}
    content = Show_Ji.objects.all()
    response['data'] = []
    for con in content:
        response['data'].append(to_dict(con))

    return JsonResponse(response)


@require_http_methods(['GET'])
def get_wen_content(request):
    response = {'code': 0, 'message': 'success'}
    wen_id = request.GET.get('id')
    if Show_Wen.objects.filter(type_id=wen_id).count() != 0:
        response['data'] = to_dict(Show_Wen.objects.get(type_id=wen_id))
        response['status'] = 1
    else:
        response['data'] = []
        response['status'] = 0
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_wen_detail(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    wen_id = request.GET.get('id')
    if Show_Wen.objects.filter(type_id=wen_id).count() != 0:
        type_id = Show_Wen.objects.get(type_id=wen_id).id
        if Wen_Table.objects.filter(category=Show_Wen(id=type_id)).count() != 0:
            details = Wen_Table.objects.filter(category=Show_Wen(id=type_id))
            for detail in details:
                response['data'].append(to_dict(detail))

    return JsonResponse(response)


@require_http_methods(['GET'])
def get_wen_title(request):
    response = {'code': 0, 'message': 'success'}
    card_id = request.GET.get('card_id')
    wen = Wen_Table.objects.get(id=card_id)
    title = wen.title
    content = wen.content
    response['title'] = title
    response['content'] = content
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_wen_comment(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    wen_id = request.GET.get('id')
    comment_num = Wen_Comment.objects.filter(wen=Wen_Table(id=wen_id)).count()
    if comment_num != 0:
        comment_list = Wen_Comment.objects.filter(wen=Wen_Table(id=wen_id))
        for comment in comment_list:
            user_id = comment.user
            username = user_id.username
            comment_dict = to_dict(comment)
            comment_dict['username'] = username
            response['data'].append(comment_dict)

    return JsonResponse(response)


@require_http_methods(['POST'])
def add_wen_comment(request):
    response = {'code': 0, 'message': 'success'}
    body = json.loads(request.body)
    user_id = body.get('user_id')
    comment = body.get('comment')
    wen_id = body.get('card_id')
    add_comment = Wen_Comment(user=UserProfile(id=user_id), comment=comment, wen=Wen_Table(id=wen_id))
    add_comment.save()
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_material_life_detail(request):
    response = {'code': 0, 'message': 'success'}
    material_id = request.GET.get('id')
    details_count = Material_Detail.objects.filter(type_id=material_id).count()
    if details_count != 0:
        response['code'] = 1
        details = Material_Detail.objects.get(type_id=material_id)
        details = to_dict(details)
        img_src = details['img']
        img_list = img_src.split(',')
        details['img'] = img_list
        response['data'] = details
    return JsonResponse(response)


