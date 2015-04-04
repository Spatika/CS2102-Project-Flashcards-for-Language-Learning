from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
import logging

logger = logging.getLogger(__name__)

def index(request):
	template = loader.get_template('quiz/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def login_user(request):
	template = loader.get_template('quiz/dashboard.html')
	logger.debug("login_user_called")
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
