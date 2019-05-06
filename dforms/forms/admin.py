from django.contrib import admin

from .models import Form, Question, Choice

# admin.site.register(Question)


admin.site.site_header = "Survey Admin"


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 1


class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [QuestionsInline]
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Form, FormAdmin)
