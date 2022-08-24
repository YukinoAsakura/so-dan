from django.urls import path ,include
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('quest',views.quest, name='quest'),
    path('',views.index,name ='top'),
    path('mypage',views.mypage,name ='mypage'),
    path('hello', views.hello, name='hello'),
    path('<int:article_id>/',views.detail,name='detail'),
    path('<int:article_id>/delete', views.update, name='delete'),
    path('<int:article_id>/update', views.update, name='update'),
    path('redirect',views.redirect_test, name='redirect_test')
]