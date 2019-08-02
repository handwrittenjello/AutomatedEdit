from django.contrib import admin


# Register your models here.
from .models import Question, Choice, Fightcard


class ChoiceInline(admin.TabularInline):
    model = Choice
#    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('card')]}),
        (None,				 {'fields': [('weightclass')]}),
        (None,				 {'fields': [('winner')]}),
        (None,				 {'fields': [('defeat')]}),
        (None,				 {'fields': [('loser')]}),
        (None,				 {'fields': [('wonby')]}),
        (None,				 {'fields': [('roundin')]}),
        (None,				 {'fields': [('time')]}),

        
    ]
    inlines = [ChoiceInline]
    list_display = ('card', 'weightclass', 'winner', 'defeat', 'loser',
    		'wonby', 'roundin', 'time')
#    list_filter = ['card']
    search_fields = ['card']

class Fightcard(admin.ModelAdmin):
    model = Fightcard
    list_display = ('weight_class', 'winner', 'def_field', 'loser', 'won_by', 'round', 'time', 'card')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(Fightcard)