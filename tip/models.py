from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.
class BettingTip(models.Model):
    country = CountryField(blank_label='(select country)', default="England")
    home_team = models.CharField(max_length=30)
    away_team = models.CharField(max_length=30)
    prediction = models.CharField(max_length=20)
    odds = models.FloatField()
    analysis = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_title(self):
        return self.home_team + ' - ' + self.away_team + ' (' + self.prediction + ')'

    def __str__(self):
        return self.get_title()
