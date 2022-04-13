from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from account import views as accountviews
app_name = 'app'

urlpatterns =[
    path('', views.main, name='main'),
    path('practice/', views.main, name='practice'),
    path('exam/', views.main, name='exam'),
    path('quizreg/', views.main, name='quizreg'),
    path('mypage/', accountviews.mypage, name='mypage'),
]