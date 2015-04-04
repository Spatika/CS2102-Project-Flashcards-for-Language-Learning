from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

def index(request):
	template = loader.get_template('quiz/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def login_user(request):
	context = {}
	context.update(csrf(request))
	username = password = ''
	# This is when submit is already clicked once
	if request.POST:
		username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        state = 'not logged in'
        if user is not None:
			login(request, user)
			state = "You're successfully logged in!"
	return render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password})


def signup_user(request):
	context = {}
	context.update(csrf(request))
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
        password = request.POST.get('password')
        # creating a new user
        user = User.objects.create_user(username, username, password)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        authenticate(username=username, password=password)
        login(request, user)
	return render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password})