from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context ={}
	context['hello']='Hello World'
	return render(request,'index.html',context)

def gitblog(request):
	context={}
	context['gitblog']='gitblog'
	return render(request,'gitblog.html',context)