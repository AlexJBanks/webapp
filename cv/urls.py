from django.urls import path

from . import views

urlpatterns = [
    path('', views.cv_list, name='cv'),
    path('basic/<int:pk>/', views.basic_edit, name='basic_edit'),
    path('basic/new/', views.basic_new, name='basic_new'),
    path('education/<int:pk>/', views.education_edit, name='education_edit'),
    path('education/new/', views.education_new, name='education_new'),
    path('work/<int:pk>/', views.work_edit, name='work_edit'),
    path('work/new/', views.work_new, name='work_new'),
    path('education/<int:epk>/grade/<int:gpk>/', views.grade_edit, name='grade_edit'),
    path('education/<int:epk>/grade/new/', views.grade_new, name='grade_new'),
]
