from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.
class ChoiceInline(admin.StackedInline):# use either (admin.TabularInline)
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fields name',      {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', )
    inlines = [ChoiceInline]
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add choice',   {'fields': ['question']}),
        ('Add question', {'fields': ['choice_text']}),
        ('Give vote',    {'fields': ['votes']}),
    ]
    list_display = ('question', 'choice_text','votes' )



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)