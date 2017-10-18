from django.db import models
from django import forms
# Create your models here.

gender=[("Male"),("Female")]

class Person(models.Model):
	def __str__(self):
		return str(self.aadhaar)
	def fullname(self):
		return first_name,last_name

	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	sex=forms.ChoiceField(choices=gender,widget=forms.RadioSelect())
	address=models.CharField(max_length=1000)
	aadhaar=models.IntegerField("Player No.")

	
		

class Stat(models.Model):
	def __str__(self):
		return str(self.aadhaar)

	aadhaar=models.ForeignKey(Person,null=True,)
	hundreds=models.IntegerField(null=True)
	fifties=models.IntegerField(null=True)
	sixes=models.IntegerField(null=True)
	fours=models.IntegerField(null=True)
	strike_rate=models.IntegerField("Strike Rate",null=True)
	average=models.IntegerField(null=True)
	
