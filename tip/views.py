from django.shortcuts import render
from . models import BettingTip, BetPawaTip

# Create your views here.
def tip(request):
	tips = BettingTip.objects.all()
	return render(request, "addtip.html", {'tips': tips})

def multiple(request):
	multi = BetPawaTip.objects.all()
	return render(request, "multiplebet.html", {'multi': multi})
