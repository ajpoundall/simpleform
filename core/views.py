from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
	if request.method =='POST':
		form = forms.CreatePerson(request.POST)
		if form.is_valid():
			form.save()


	else:
		form = forms.CreatePerson()

	return render(request, 'index.html', {'form':form})