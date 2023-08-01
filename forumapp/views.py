from django.shortcuts import render

from .models import Questions, Answers


from django import template

register = template.Library()



# Create your views here.
@register.filter
def questions_list(request):
    questions = Questions.objects.all()
    answers = Answers.objects.all()

    context = {
        'questions':questions,
        'answers' : answers,
    }

    return render(request, 'forumapp/questions_list.html', context)