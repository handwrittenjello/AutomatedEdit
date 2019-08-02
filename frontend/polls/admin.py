from django.contrib import admin


# Register your models here.
from .models import Question, Choice, Fightcard


class ChoiceInline(admin.StackedInline):
    model = Choice
#    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('card')]}),
        (None,				 {'fields': [('winner')]}),
        
    ]
    inlines = [ChoiceInline]
    list_display = ('card', 'winner')
 #   list_filter = ['Winner']
    search_fields = ['card']

class Fightcard(admin.ModelAdmin):
    model = Fightcard
    list_display = ('weight_class', 'winner', 'def_field', 'loser', 'won_by', 'round', 'time', 'card')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(Fightcard)