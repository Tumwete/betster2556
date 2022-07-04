from django.shortcuts import render
from . models import BettingTip

# Create your views here.
def tip(request):
	tips = BettingTip.objects.all()
	return render(request, "addtip.html", {'tips': tips})

