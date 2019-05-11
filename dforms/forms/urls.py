from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('forms/<int:form_id>/', views.question_view, name='question_view'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
