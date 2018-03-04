from django.shortcuts import render
from .models import Hisab


# Create your views here.
def index(request):
	expenses = Hisab.objects.all()
	context = {'expenses': expenses}
	return render(request,'hisab.html', context)


