from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from quiz.models import Set
import logging

logger = logging.getLogger(__name__)

def index(request):
	template = loader.get_template('quiz/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def login_user(request):
	context = {}
	context.update(csrf(request))
	username = password = state = ''
	# This is when submit is already clicked once
	if request.POST:
		username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # Actual authenticated user
        if user is not None:
			# Successful login scenario
			login(request, user)
			state = "You're successfully logged in!"
			user_name = username
			user_id = User.objects.filter(username=username)
			sets = Set.objects.filter(user=user_id)
			return render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password, 'sets': sets})
	state="Invalid login credentials"
	return render(request, 'quiz/index.html', {'state': state})

def debug_view(request):
	template = loader.get_template('quiz/dashboard.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

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
        state = "New user created successfully"
	return render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password})