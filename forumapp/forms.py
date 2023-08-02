from django import forms
from .models import Questions, Answers


class AddQuestions(forms.ModelForm):
    class Meta:
        model = Questions
        exclude =('author',)



class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answers
        exclude =('author',)