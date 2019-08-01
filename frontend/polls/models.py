from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Question(models.Model):
#    question_text = models.CharField(max_length=200)
    polls_question = models.CharField(db_column='Winner',max_length=200)
 #   pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.polls_question
 #   def was_published_recently(self):
 #       now = timezone.now()
 #       return now - datetime.timedelta(days=1) <= self.pub_date <= now
 #   was_published_recently.admin_order_field = 'pub_date'
 #   was_published_recently.boolean = True
 #   was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Fightcard(models.Model):
    index = models.IntegerField(db_column='Index', blank=True, null=True, default='')  # Field name made lowercase.
    weight_class = models.TextField(db_column='WeightClass', blank=True, null=True, default='')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    winner = models.TextField(db_column='Winner', blank=True, null=True, default='')  # Field name made lowercase.
    def_field = models.TextField(db_column='def', blank=True, null=True, default='')  # Field renamed because it was a Python reserved word.
    loser = models.TextField(db_column='Loser', blank=True, null=True, default='')  # Field name made lowercase.
    won_by = models.TextField(db_column='WonBy', blank=True, null=True, default='')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    round = models.TextField(db_column='Round', blank=True, null=True, default='')  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True, default='')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True, default='')  # Field name made lowercase.
    card = models.TextField(db_column='Card', blank=True, null=True, default='')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fightcard'