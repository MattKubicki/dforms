from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('forms/<int:form_id>/', views.question_view, name='question_view'),
    path('login', views.login_view, name='login'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('forms', views.UserAnnouncesList.as_view(), name='forms'),
    path('createform', views.create_form, name='createform'),
    path('<int:question_id>/vote/', views.vote_question, name='vote'),
    path('filled/<int:form_id>', views.filled, name='filled'),
    path('posted', views.posted, name='posted'),
    path('forms/removed/<int:form_id>', views.remove_form, name='delete_view'),
    path('forms/edit/<int:form_id>', views.edit_form, name='form_view')
]
