from django.urls import path

from .views import Questions, details, create_question, delete_question, edit_question

urlpatterns = [
    path('', Questions.as_view(), name='questions_list'),
    path('details/<int:pk>', details, name='details'),
    path('create_question', create_question, name='create_question'),
    path('delete_question/<int:pk>', delete_question, name='delete_question'),
    path('edit_question/<int:pk>', edit_question, name='edit_question'),
]
