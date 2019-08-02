from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class cardkey(models.Model):
    cardkey = models.CharField(db_column='card_id',max_length=200)

    class Meta:
        managed = False
        db_table = 'polls_question'
class Question(models.Model):
#    question_text = models.CharField(max_length=200)
    card = models.ForeignKey(cardkey,on_delete=models.CASCADE
    )
 #   pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.card
    winner = models.CharField(db_column='Winner',max_length=200,)
    weightclass = models.CharField(db_column='WeightClass',max_length=200)
    loser = models.CharField(db_column='Loser',max_length=200)
    defeat = models.CharField(db_column='def',max_length=200)
    wonby = models.CharField(db_column='WonBy',max_length=200)
    roundin = models.CharField(db_column='Round',max_length=200)
    time = models.CharField(db_column='Time',max_length=200)
 #   winner = models.CharField(db_column='Winner',max_length=200)

 #   def was_published_recently(self):
 #       now = timezone.now()
 #       return now - datetime.timedelta(days=1) <= self.pub_date <= now
 #   was_published_recently.admin_order_field = 'pub_date'
 #   was_published_recently.boolean = True
 #   was_published_recently.short_description = 'Published recently?'
    class Meta:
        managed = False
        db_table = 'polls_choice'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    winner = models.CharField(db_column='Winner',max_length=200)
    weightclass = models.CharField(db_column='WeightClass',max_length=200)
    loser = models.CharField(db_column='Loser',max_length=200)
    defeat = models.CharField(db_column='def',max_length=200)
    wonby = models.CharField(db_column='WonBy',max_length=200)
    roundin = models.CharField(db_column='Round',max_length=200)
    time = models.CharField(db_column='Time',max_length=200)

#    votes = models.IntegerField(default=0)
#    def __int__(self):
#        return self.ufcCard
    class Meta:
        managed = False
        db_table = 'polls_choice'

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