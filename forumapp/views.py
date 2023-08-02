from django.shortcuts import render, redirect

from django.views.generic import ListView



from .models import Questions, Answers
from .forms import AddQuestions, AddAnswer




# Create your views here.

class Questions(ListView):
    model = Questions



def details(request, pk):
    question = Questions.objects.get(id=pk)
    answers = Answers.objects.filter(questions=question)

    if request.method == 'POST':
        form_answer = AddAnswer(request.POST)
        if form_answer.is_valid():
            myform =form_answer.save(commit=False)
            myform.author = request.user
            myform.questions = question
            myform.save()
    else:
        form_answer = AddAnswer()
    
    context = {
        'question':question,
        'answers':answers,
        'form_answer':form_answer
    }
    return render (request, 'forumapp/questions_details.html',context )


def create_question(request):
    if request.method == 'POST':
        form = AddQuestions(request.POST, request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.author = request.user
            myform.save()

        return redirect('/')

    else:
        form = AddQuestions()

    return render(request, 'forumapp/create_question.html', {'form':form})


def edit_question(request):
    pass 



def delete_question(request, pk):
    question = Questions.objects.get(id=pk)
    question.delete()
    return redirect('/')