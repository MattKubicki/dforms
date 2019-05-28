from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from forms.additional_forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy
from .user_forms import CustomUserCreationForm
from .models import Form, Question, Choice

from forms.models import Form

def main_view(request):
    latest_forms_list = Form.objects.order_by('-pub_date')[:5]
    context = {'latest_forms_list': latest_forms_list}
    if request.user.is_authenticated:
        return render(request, 'home.html', context) #switched from main to home, which extends main
    else:
        return render(request, 'not_logged.html') #further redirects to login site
# Create your views here.


def login_view(request):
    return render(request, 'registration/login.html')


def filled(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    return render(request, 'filled.html', {'form': form})


def posted(request):
    return render(request, 'posted.html')


def question_view(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    return render(request, 'question_view.html', {'form': form})


def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form_id = question.form_id
    form = form_id
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'question_view.html', {
            'form': form,
            'error_message': "No choice selected"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return render(request, 'question_view.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('main_view')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
def user_forms_view(request):
    return render(request, 'forms.html')


def create_form(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            form = Form()
            form.name = request.POST.get('name')
            form.owner_id = request.user
            form.save()
            print(form.name)
            return render(request, 'createform.html')
    else:
        return render(request, 'createform.html')
