from ...model_package.buy.buy_models import buy_record, Goods, Categories
from ...model_package.people.people_models import workman
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from ...utils import to_dict
import json
from django.db.models import Q


@require_http_methods(['GET'])
def get_total_goods_num(request):
    response = {'code': 0, 'message': 'success'}
    number = Goods.objects.all().count()
    response['data'] = number
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_categories(request):
    response = {'code': 0, 'message': 'success'}
    categories = Categories.objects.all()
    response['data'] = []
    for cate in categories:
        response['data'].append(to_dict(cate))
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_workman(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    workmans = workman.objects.all()
    for person in workmans:
        response['data'].append(to_dict(person))
    return JsonResponse(response)


@require_http_methods(['POST'])
def get_goods_info(request):
    response = {'code': 0, 'message': 'success'}
    response['data'] = []
    data = json.loads(request.body)
    person_id = data.get('person')
    category_id = data.get('category')
    if len(person_id) == 0 and len(category_id) == 0:
        goods_set = Goods.objects.all()
    else:
        condition_query_person = None
        condition_query_category = None
        for id in person_id:
            if condition_query_person is None:
                condition_query_person = Q(person=workman(id=id))
            else:
                condition_query_person = condition_query_person | Q(person=workman(id=id))
        for id in category_id:
            if condition_query_category is None:
                condition_query_category = Q(category=Categories(id=id))
            else:
                condition_query_category = condition_query_category | Q(category=Categories(id=id))

        if condition_query_person is None:
            condition_query = condition_query_category
        elif condition_query_category is None:
            condition_query = condition_query_person
        else:
            condition_query = condition_query_person & condition_query_category

        goods_set = Goods.objects.filter(condition_query)
    for good in goods_set:
        pay_count = buy_record.objects.filter(goods=Goods(id=good.id)).count()
        good_dict = to_dict(good)
        good_dict['pay_count'] = pay_count
        response['data'].append(good_dict)
    return JsonResponse(response)
