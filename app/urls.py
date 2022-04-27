from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'


urlpatterns =[
    path('', views.main, name='main'),
    path('practice/', views.main, name='practice'),
    path('exam/', views.main, name='exam'),
    path('quizreg/', views.quizenroll_1, name='quizreg'),
    
    path('manage/', views.manage, name='manage'),
    #path('manage/<int:userid>', views.Class, name='class'),
    
    path('manage/delete/<int:deleteid>', views.class_delete, name='class_delete'),
    path('manage/delete/<int:classid>/<int:quizdeleteid>', views.quiz_delete, name='quiz_delete'),
    
    path('manage/quiz/<int:class_id>', views.quiz_student_print, name='quiz_student_print'),
    path('manage/<int:classid>/<int:quizid>', views.student_print, name='student_print'),
    
    path('manage/enroll', views.enroll, name='enroll'),
    
    #quizreg
    
    path('quizreg/1/', views.quizreg_1, name='quizreg_1'),
]


#모든가능성