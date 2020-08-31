from django.urls import path

from . import views

urlpatterns = [
    path('', views.cv_list, name='cv'),
    path('b/new/', views.basic_new, name='basic_new'),
    path('b/<int:pk>/', views.basic_edit, name='basic_edit'),
    path('e/new/', views.education_new, name='education_new'),
    path('e/<int:pk>/', views.education_edit, name='education_edit'),
    path('e/<int:epk>/new/', views.grade_new, name='grade_new'),
    path('e/<int:epk>/<int:gpk>/', views.grade_edit, name='grade_edit'),
    path('w/new/', views.work_new, name='work_new'),
    path('w/<int:pk>/', views.work_edit, name='work_edit'),
]
