from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('forms/<int:form_id>/', views.question_view, name='question_view'),
    path('login', views.login, name='login'),
]
