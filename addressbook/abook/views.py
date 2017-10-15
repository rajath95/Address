from django.shortcuts import render

from django.http import HttpResponse
from abook.models import Person
def index(request):
	output="The players in the database are:  "
	profile=Person.objects.all()
	for i in profile:
		output+=i.first_name
		output+=" "
		output+=i.last_name
		output+='   '
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You're looking at the home page of  %s" % question_id)

def stats(request,question_id):
	response = "You're looking at the stats profile page %s"
	return HttpResponse(response% question_id)






