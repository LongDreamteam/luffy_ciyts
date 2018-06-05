"""luffycity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from luffy.view import course_view,login_view,article_view,price_view,micro_view

urlpatterns = [
    #登录
    url(r'^login/$', login_view.LoginView.as_view()),
    #注册
    # url(r'register/$', views.RegisterView.as_view()),
    #注销
    #首页
    # url(r'^index/$', views.IndexView.as_view()),
    #---------------------------------------------------------------------------------


    #课程
    url(r'^course/$', course_view.CourseView.as_view({'get': 'list'})),
    #课程详细
    url(r'^course/(?P<pk>\d+)$', course_view.CourseView.as_view({'get': 'retrieve'})),
    #价格策略
    url(r'^price_policy/(?P<course_id>\d+)/$', price_view.PricePolicyView.as_view()),
    #---------------------------------------------------------------------------------



    #学位课程
    url(r'^micro/$', micro_view.MicroView.as_view({'get': 'list'})),
    #课程详细
    url(r'^other/(?P<pk>\d+)$', micro_view.MicroView.as_view({'get': 'retrieve'})),
    #-----------------------------------------------------------------------------------


    #深科技，文章列表
    url(r'^article/$', article_view.ArticleView.as_view({'get': 'get'})),
    #深科技，文章详细
    url(r'^article/(?P<pk>\d+)/$',article_view.ArticleView.as_view({'get': 'retrieve'})),

]
