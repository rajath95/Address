from django.conf.urls import url

from . import views

urlpatterns=[ url(r'^$',views.index,name='index'),
			url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
			url(r'^stats/(?P<question_id>[0-9]+)$',views.stats,name='stats'),	
			url(r'^addstats/(?P<player_id>[0-9]+)$',views.addstats,name='addstats'),
			url(r'^addplayer/$',views.addplayer,name='addplayer')
			] 
