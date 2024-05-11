from django.views.decorators.http import require_http_methods
from ...model_package.news.news_model import News
from ...utils import to_dict
from django.http import JsonResponse


@require_http_methods(['GET'])
def get_news(request):
    response = {'code': 0, 'message': 'success'}
    news_list = News.objects.all()
    response['data'] = []
    for news in news_list:
        response['data'].append(to_dict(news))

    return JsonResponse(response)


@require_http_methods(['GET'])
def get_specific_news(request):
    response = {'code': 0, 'message': 'success'}
    id = request.GET.get('id')
    news = News.objects.get(id=id)
    response['news'] = to_dict(news)
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_show_news(request):
    response = {'code': 0, 'message': 'success'}
    id = int(request.GET.get('id'))
    response['data'] = []
    if id == 0:
        news = News.objects.filter(sub_title='比赛')
    elif id == 1:
        news = News.objects.filter(sub_title='展览')
    elif id == 2:
        news = News.objects.filter(sub_title='活动')
    else:
        news = News.objects.filter(sub_title='培训')

    for item in news:
        response['data'].append(to_dict(item))

    return JsonResponse(response)