from django.urls import path
from . import views

urlpatterns = [

    path('', views.course_list, name = 'course-home-path'),
    path('course-detail/<int:pk>/', views.course_detail, name = 'course-detail-path'),
]