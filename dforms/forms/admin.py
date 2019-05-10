from django.contrib import admin
from django.forms import BooleanField

from .models import Form, Question, Choice

# admin.site.register(Question)


admin.site.site_header = "Survey Admin"


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 1
    fieldsets = [
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['is_open_question']}),
    ]


class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [QuestionsInline]
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Form, FormAdmin)
