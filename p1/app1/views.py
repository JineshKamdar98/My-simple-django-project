from django.shortcuts import render
#from django.template import loader
#from .models import Channel

def f1(request):
	#all=Channel.objects.all()
	return render(request,"page.html",{})

def f2(request):
	return render(request,"p2.html",{})
