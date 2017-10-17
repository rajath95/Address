from django import forms

class ContactForm(forms.Form):
	
	runs=forms.IntegerField()
	hundreds=forms.IntegerField()
	fifties=forms.IntegerField()
	sixes=forms.IntegerField(label="6s")
	fours=forms.IntegerField(label="4s")
	strike_rate=forms.IntegerField(label="Strike Rate")
	average=forms.IntegerField()


class PlayerForm(forms.Form):
	first_name=forms.CharField()
	last_name=forms.CharField()
	address=forms.CharField()

