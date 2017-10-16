from django.shortcuts import render,get_object_or_404
from django.template import loader

from django.http import HttpResponse
from abook.models import Person
def index(request):
	output="The players in the database are:  "
	profile=Person.objects.all()
	template=loader.get_template("abook/index.html")
	context={"profile":profile}

	return HttpResponse(template.render(context,request))

def detail(request, question_id):
	
	person1=get_object_or_404(Person,pk=question_id)
	return render(request,'abook/detail.html',{'person':person1})

	#template=loader.get_template("abook/detail.html")
	#context={"profile":profile}
	#for i in profile:
	#	objectnme=str(i)
	#	if objectnme==question_id:
	#		right_object=i
	#		name=objectnme
	#	if i==question_id:#if i is question_id:
	#		name=i.first_name
	#return HttpResponse(template.render(context,request))	
	#return HttpResponse("You're looking at the home page of  %s %s" % (right_object.first_name ,right_object.last_name))

def stats(request,question_id):
	person1=get_object_or_404(Person,pk=question_id)
	return render(request,'abook/stats.html',{'person':person1})
	#response = "You're looking at the stats profile page %s %s" % (person1.first_name,person1.last_name)	
	#return HttpResponse(response)


#def addplayer(request):




