from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from forms.models import Form


def main_view(request):
    return render(request, 'main.html')
# Create your views here.


def login(request):
    return render(request, 'login.html')


def question_view(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    return render(request, 'question_view.html', {'form': form})
