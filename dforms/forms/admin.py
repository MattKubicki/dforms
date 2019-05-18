from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.forms import BooleanField

from .models import Form, Question, Choice
from .user_forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# admin.site.register(Question)

admin.site.site_header = "Survey Admin"


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 1
    fieldsets = [
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['is_open_question']}),
    ]

#
# class FormAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']}),
#     ]
#     inlines = [QuestionsInline]
#     list_display = ['name']
#     search_fields = ['name']


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)
