from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from forms.models import Form


def index(request):
    return HttpResponse("XDDDDDDDDDDD")
# Create your views here.


def detail(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    return render(request, 'detail.html', {'form': form})
