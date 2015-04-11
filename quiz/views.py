from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from .models import Card, Set, Language
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import logging
import json

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
			response = HttpResponse()
			response = render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password, 'sets': sets, 'number_of_sets': len(sets)})
			# response.set_cookie('user', username)
			return response
	state = "Invalid login credentials"
	return render(request, 'quiz/index.html', {'state': state})

def debug_view(request):
	template = loader.get_template('quiz/createSet.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def signup_user(request):
	context = {}
	context.update(csrf(request))
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = User.objects.create_user(username, username, password)
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		user.save()
        authenticate(username=username, password=password)
        login(request, user)
        state = "New user successfully created"
        response = HttpResponse()
        response = render(request, 'quiz/dashboard.html' ,{'state':state, 'username': username, 'password': password})
        # response.set_cookie('user', username)
        return response
	return render(request, 'quiz/dashboard.html' ,{'state': 'Error occured', 'username': username, 'password': password})

def create_set_form(request):
	return render(request, 'quiz/createSet.html', { 'languages': Language.objects.all() })

def userPage(request):
	template = loader.get_template('quiz/userPage.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def search(request):
	print("In search")
	template = loader.get_template('quiz/userPage.html')
	if request.POST:
		decode_json = request.POST.get('srch-term')
		user_sets = Set.objects.filter(
			Q(title__contains=decode_json)|
			Q(description__contains=decode_json)|
			Q(language_from__name__contains=decode_json)|
			Q(language_to__name__contains=decode_json)
			).filter(user__username='supraja')
		print(user_sets)
		other_sets = Set.objects.filter(
			Q(title__contains=decode_json)|
			Q(description__contains=decode_json)|
			Q(language_from__name__contains=decode_json)|
			Q(language_to__name__contains=decode_json)
			).filter(~Q(user__username='supraja'))
		print(other_sets)
		context = {'UserSets':user_sets, 'OtherSets':other_sets}
	return HttpResponse(template.render(context))

def set_create(request):
	context = {}
	context.update(csrf(request))
	retrieved_user = User.objects.get(username=request.user)
	sets = Set.objects.filter(user=retrieved_user)
	if request.POST:
		request_title = request.POST.get('title')
		request_description = request.POST.get('description')
		request_language_to = request.POST.get('languageTo')
		request_language_from = request.POST.get('languageFrom')
		retrieve_language = lambda x: Language.objects.get(pk=x)
		created_set = Set(user = retrieved_user, 
			title = request_title, 
			description = request_description, 
			language_to = retrieve_language(request_language_to),
			language_from = retrieve_language(request_language_from))
		created_set.save()
		state = "New set successfully created"
		return render(request, 'quiz/dashboard.html' ,{'state':'successfully created set', 'sets': sets, 'number_of_sets': len(sets)})
	else:
		return render(request, 'quiz/dashboard.html' ,{'state':'Could not create set', 'sets': sets, 'number_of_sets': len(sets)})

def get_set(request):
	template = loader.get_template('quiz/cards.html')
	#data = json.loads(request.body)
	#user_set_data = data['set'] 
	#set_cards  = Card.objects.filter(title_contains= user_set_data['title'])
	set_cards = Card.objects.filter(set__title = 'A1 Spanish')
	print(set_cards)
	context = {'SetCards':set_cards}
	return HttpResponse(template.render(context))
