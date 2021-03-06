from django.contrib import admin
from django.contrib.auth.models import User
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Question--',  {'fields':['question_text']}),
            ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']}),
            ]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']

    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(User)
