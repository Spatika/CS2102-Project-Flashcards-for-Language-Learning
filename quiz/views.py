from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from .models import Card, Set, Language
import json

from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from quiz.models import Set
import logging

logger = logging.getLogger(__name__)

from django.db.models import Q
from quiz.models import *
import json

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
			return render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password, 'sets': sets, 'number_of_sets': len(sets)})
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

def userPage(request):
	template = loader.get_template('quiz/userPage.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

# def search(request,user_id):
def search(request):
	template = loader.get_template('quiz/userPage.html')
	if request.POST:
		decode_json = request.POST.get('srch-term')
		user_sets = Set.objects.filter(
			Q(title__contains=decode_json)|
			Q(description__contains=decode_json)|
			Q(language_from__name__contains=decode_json)|
			Q(language_to__name__contains=decode_json)
			).filter(user__name='shweta')
		print(user_sets)
		other_sets = Set.objects.filter(
			Q(title__contains=decode_json)|
			Q(description__contains=decode_json)|
			Q(language_from__name__contains=decode_json)|
			Q(language_to__name__contains=decode_json)
			).filter(~Q(user__name='shweta'))
		print(other_sets)
		context = {'UserSets':user_sets, 'OtherSets':other_sets}
	return HttpResponse(template.render(context))

def set_create(request):
	data = json.loads(request.body)
	user_set_data = data['set']
	user_set = Set(user=User.objects.get(pk=user_set_data['user']), 
		title=user_set_data['title'], 
		description=user_set_data['description'], 
		language_to=Language.objects.get(pk=user_set_data['language_to']), 
		language_from=Language.objects.get(pk=user_set_data['language_from']))
	user_set.save()
	user_set_cards = user_set_data['cards']
	for card in user_set_cards:
		user_set_card = Card(term=card['term'],
			definition=card['definition'],
			set=Set.objects.get(title=user_set_data['title'], 
				user=User.objects.get(pk=user_set_data['user'])))
		user_set_card.save()
	return HttpResponse()
