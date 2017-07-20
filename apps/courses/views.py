# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index(request):
	context = {
	 'courses': Course.objects.all(),
	 'messages': get_messages(request)
	}
	return render(request, 'courses/index.html', context)

def add(request):
	if request.method == "POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag,error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')
		else:
			Course.objects.create(name=request.POST['name'], description=request.POST['desc'])
			return redirect('/')
	else:
		return redirect('/')

def destroy(request, id):
	context = {
		'course': Course.objects.get(id=id)
	}
	return render(request, 'courses/destroy.html', context)

def remove(request, id):
	if request.method == "POST":
		course = Course.objects.get(id=id)
		course.delete()
		return redirect('/')
	else:
		return redirect('/')