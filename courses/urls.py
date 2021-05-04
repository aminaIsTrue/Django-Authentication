from django.urls import path
from . import views

urlpatterns = [

    path('', views.course_list, name = 'course-home-path'),
    path('course-detail/<int:pk>/', views.course_detail, name = 'course-detail-path'),
    path('course-create/', views.create_course, name = 'course-create-path'),
    path('course-update/<int:id>/', views.update_course, name = 'course-update-path'),
    path('course-delete/<int:id>/', views.delete_course, name = 'course-delete-path'),
]