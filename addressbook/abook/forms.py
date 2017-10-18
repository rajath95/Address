from django import forms

from .models import Person
from .models import Stat


class StatForm(forms.ModelForm):
	
	class Meta:
		model=Stat
		fields=["aadhaar","hundreds","fifties","sixes","fours","strike_rate","average"]




	#runs=forms.IntegerField()
	#hundreds=forms.IntegerField()
	#fifties=forms.IntegerField()
	#sixes=forms.IntegerField(label="6s")
	#fours=forms.IntegerField(label="4s")
	#strike_rate=forms.IntegerField(label="Strike Rate")
	#average=forms.IntegerField()


class PlayerForm(forms.ModelForm):
	class Meta:
		model=Person
		fields=["aadhaar","first_name","last_name"]
		

	#def clean_first_name(self):
	#	id1=self.cleaned_data.get('first_name')
	#	print (id1)
	#	if id1 == '0':
	#		raise forms.ValidationError("Please enter valid name")
	#	return id1	
		#pid=forms.IntegerField()
	#first_name=forms.CharField()
	#last_name=forms.CharField()
	#address=forms.CharField()

