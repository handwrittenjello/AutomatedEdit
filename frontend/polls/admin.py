from django.contrib import admin

from .models import Question, Choice, Fightcard


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class Fightcard(admin.TabularInline):
	model = Fightcard
	list_display = ('weight_class', 'winner', 'def_field', 'loser', 'won_by', 'round', 'time', 'card')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Fightcard)