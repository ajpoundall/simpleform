from django import forms
from . import models 

class CreatePerson(forms.ModelForm):
	class Meta:
		model = models.people
		fields = ['first_name', 'last_name']