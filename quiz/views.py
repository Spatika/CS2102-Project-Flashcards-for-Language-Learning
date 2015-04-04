from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from .models import Card, Set, User, Language
import json

def index(request):
	template = loader.get_template('quiz/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def create_set(request):
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