from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from forms.additional_forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy
from .user_forms import CustomUserCreationForm



from forms.models import Form


def main_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html') #switched from main to home, which extends main
    else:
        return render(request, 'not_logged.html') #further redirects to login site
# Create your views here.


def login_view(request):
    return render(request, 'registration/login.html')


def question_view(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
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
    return render(request, 'createform.html')
