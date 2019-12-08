from django.shortcuts import render, redirect
from . import forms
from .models import people
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	if request.method =='POST':
		form = forms.CreatePerson(request.POST)
		if form.is_valid():
			form.save()
			return redirect('overview')


	else:
		form = forms.CreatePerson()

	return render(request, 'index.html', {'form':form})

def overview(request):
	peoples = people.objects.all()
	args = {"people": peoples}
	return render(request, 'overview.html', args)