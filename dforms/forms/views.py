from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

from django.urls import reverse_lazy
from .user_forms import CustomUserCreationForm
from .models import Form, Question, Choice

import matplotlib.pyplot as plt
from pylab import *
from io import BytesIO
import base64
from django.views import generic


from forms.models import Form


def remove_form(request, form_id=None):
    object = Form.objects.get(id=form_id)
    object.delete()
    return render(request, 'delete_view.html')


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

    choice_id = request.POST['choice']
    try:
        choice = get_object_or_404(Choice, pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'question_view.html', {
            'form': form,
            'error_message': "No choice selected"
        })
    else:
        choice.votes += 1
        choice.save()
    return render(request, 'filled.html', {'form': form})


def parse_form_input(request):
    if request.method == 'POST':
        if request.POST.get('form_name'):
            form = Form()
            form.name = request.POST.get('form_name')
            form.owner_id = request.user
            form.save()
            if request.POST.get('question_name[]'):
                questions_input = request.POST.getlist('question_name[]')
                size = len(questions_input)
                for i in range(0, size):
                    question = Question()
                    question.question_text = questions_input[i]
                    question.form_id = form
                    question.save()
                    index = i+1
                    getter = 'choice_name'+str(index)
                    if request.POST.get(getter):
                        choices_input = request.POST.getlist(getter)
                        for c in choices_input:
                            choice = Choice()
                            choice.choice_text = c
                            choice.question = question
                            choice.save()
    return render(request, 'posted.html')


def posted(request):
    return parse_form_input(request)


def posted_and_edit(request, form_id=None):
    if form_id is not None:
        object = Form.objects.get(id=form_id)
        object.delete()
    return parse_form_input(request)


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

class UserAnnouncesList(ListView):

    model = Form
    template_name = 'forms.html'
    context_object_name = 'all_forms_created_by_user'

    def get_queryset(self):
        return Form.objects.filter(owner_id=self.request.user).order_by('-pub_date')


def create_form(request):
    return render(request, 'createform.html')


def edit_form(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    return render(request, 'form_view.html', {'form': form})


def plot_question(request, question_id):
    question_id = request.POST.get('question')
    question = get_object_or_404(Question, pk=question_id)
    choice_votes = []
    choice_labels = []
    total_votes = 0
    for choice in question.choice_set.all():
        total_votes += choice.votes
        choice_votes.append(choice.votes)
        choice_labels.append(choice.choice_text)
    fig1, ax1 = plt.subplots()
    ax1.pie(choice_votes, labels=choice_labels, shadow=True)
    ax1.axis('equal')

    figfile = BytesIO()
    # buf.seek(0)
    # plt.show()
    plt.savefig(figfile, format='png')
    #plt.figure().savefig(buf, format='png')

    figdata_png = base64.b64encode(figfile.getvalue())
    figfile.close()
    output = figdata_png.decode('utf8')
    # with open('plot_question.html', 'w') as f:
    #     f.write(html)
    return render(request, 'plot_question.html', {'output': output})
    #return HttpResponse(encoded, content_type="image/png; base64")
    #return render(request, 'main.html')
