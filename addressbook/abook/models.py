from django.db import models
from django import forms
# Create your models here.

gender=[("Male"),("Female")]
class Person(model.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	sex=forms.ChoiceField(choices=gender,widget=forms.RadioSelect())
	