from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class BettingTip(models.Model):
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

class BetPawaTip(models.Model):
    booking_code = models.CharField(max_length = 200)
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.booking_code