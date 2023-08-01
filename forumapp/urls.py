from django.urls import path

from .views import questions_list

urlpatterns = [
    path('', questions_list, name='questions_list'),
]
