from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
	fieldsets= [
	(None, {'fields':['aadhaar']}),
	('Personal information',{'fields':['first_name','last_name','address'],'classes':['collapse']})]
	




admin.site.register(Person,PersonAdmin)

