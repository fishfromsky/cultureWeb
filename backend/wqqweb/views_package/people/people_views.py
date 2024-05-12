from django.views.decorators.http import require_http_methods
from ...model_package.people.people_models import workman, shop, zuopin, interview
from ...utils import to_dict
from django.http import JsonResponse


@require_http_methods(['GET'])
def get_all_workman(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    people = workman.objects.all()
    for p in people:
        response['data'].append(to_dict(p))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_specific_workman(request):
    response = {'code': 0, 'message': 'success'}
    info_id = request.GET.get('id')
    info = workman.objects.get(id=info_id)
    response['data'] = to_dict(info)
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_shop_info(request):
    response = {'code': 0, 'message': 'success'}
    id = request.GET.get('id')
    info = shop.objects.get(owner=workman(id=id))
    response['data'] = to_dict(info)
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_workman_zuopin(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    id = request.GET.get('id')
    works = zuopin.objects.filter(owner=workman(id=id))
    if works.count() != 0:
        for item in works:
            response['data'].append(to_dict(item))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_interview_content(request):
    response = {'code': 0, 'message': 'succuess'}
    id = request.GET.get('id')
    content_num = interview.objects.filter(owner=workman(id=id)).count()
    if content_num != 0:
        content = interview.objects.get(owner=workman(id=id))
        response['data'] = to_dict(content)
    else:
        response['data'] = {}

    return JsonResponse(response)