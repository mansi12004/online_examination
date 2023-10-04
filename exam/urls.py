from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path("test/",views.test,name = 'test'),
    path('result/',views.result,name='result'),
    path('history/', views.history, name='history'),
    path('exam_already_taken/', views.exam_already_taken, name='exam_already_taken')
]