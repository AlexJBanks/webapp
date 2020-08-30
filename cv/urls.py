from django.urls import path

from . import views

urlpatterns = [
    path('', views.cv_list, name='cv'),
    path('basic/<int:pk>/', views.basic_edit, name='basic_edit'),
    path('basic/new/', views.basic_new, name='basic_new'),
]
