from django.contrib import admin

from .models import Person,Stat
from .forms import PlayerForm,StatForm

class PersonAdmin(admin.ModelAdmin):
	list_display=["__str__","first_name","last_name","address","sex"]
	form=PlayerForm
	#class Meta:
	#	model = Person
	 	
	
class StatAdmin(admin.ModelAdmin):
	list_display=["__str__","hundreds","fifties","sixes","fours","strike_rate","average"]
	form=StatForm



admin.site.register(Person,PersonAdmin)
admin.site.register(Stat,StatAdmin)
