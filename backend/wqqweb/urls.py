from . import views
from django.conf.urls import url

urlpatterns = [
    url('login', views.login),
    url('register', views.register),

    # 评论相关
    url('get_comments', views.comment_views.get_all_comments), # 获取评论

    url('add_guanzhu', views.comment_views.add_guanzhu), # 添加关注
    url('delete_guanzhu', views.comment_views.delete_guanzhu),  # 取消关注

    url('add_dianzan', views.comment_views.add_dianzan), # 添加点赞
    url('delete_dianzan', views.comment_views.delete_dianzan), # 取消点赞

    url('add_shoucang', views.comment_views.add_shoucang),  # 添加收藏
    url('delete_shoucang', views.comment_views.delete_shoucang),  # 取消收藏

    url('get_person_info', views.comment_views.get_personal_info),  # 获取个人的点赞、评论等数据
    url('get_person_shoucang', views.comment_views.get_my_shoucang),  # 获取个人收藏
    url('get_person_guanzhu', views.comment_views.get_my_guanzhu),  # 获取个人关注列表
    url('get_hot_comment', views.comment_views.get_hot_comment),  # 获取热门评论
    url('get_person_liking', views.comment_views.get_my_dianzan),  # 获取个人点赞列表
    url('get_search_content', views.comment_views.get_search_content),   # 获取搜索内容

    url('get_news', views.news_view.get_news),  # 获取新闻
    url('get_specific_news', views.news_view.get_specific_news),  # 获取某一条新闻
    url('get_show_news', views.news_view.get_show_news),  # 获取展示新闻

    url('get_goods_number', views.buy_views.get_total_goods_num),  # 获取商品总数
    url('get_goods_categories', views.buy_views.get_categories),  # 获取商品种类
    url('get_workmans', views.buy_views.get_workman),  # 获取传承人信息
    url('get_goods_info', views.buy_views.get_goods_info),  # 获取商品详细信息

    url('get_show_ji', views.show_views.get_ji_content),  # 获取“技”页面所有信息
    url('get_show_content', views.show_views.get_wen_content),  # 获取“纹”页面信息
    url('get_wen_detail', views.show_views.get_wen_detail),  # 获取每一个“纹”下详细信息
    url('get_wen_title', views.show_views.get_wen_title),  # 获取具体的“纹”介绍标题
    url('get_wen_comment', views.show_views.get_wen_comment),  # 获取“纹”评论
    url('add_wen_comment', views.show_views.add_wen_comment),  # 添加“纹"评论

    url('get_material_detail', views.show_views.get_material_life_detail),  # 获取“物”

    url('get_history_info', views.show_views.get_history_info),  # 获取“史”信息

    url('get_all_workman', views.people_views.get_all_workman),  # 获取所有工匠信息
    url('get_workman_info', views.people_views.get_specific_workman),  # 获取“匠”具体信息
    url('get_shop_info', views.people_views.get_shop_info),   # 获取“匠”具体信息
    url('get_workman_zuopin', views.people_views.get_workman_zuopin),  # 获取“匠”作品
    url('get_interview_content', views.people_views.get_interview_content),  # 获取采访内弄
]