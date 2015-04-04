from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Q
from quiz.models import *
import json

def index(request):
	template = loader.get_template('quiz/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def search(request):
	decode_json = json.loads(request.body)
	print(decode_json)
	# decode_json = 'German'
	template = loader.get_template('quiz/index.html')
	sets = Set.objects.filter(
		Q(title__contains=decode_json)|
		Q(description__contains=decode_json)|
		Q(language_from__name__contains=decode_json)|
		Q(language_to__name__contains=decode_json)
		)
	print(sets)
	context = {'Sets':sets}
	return HttpResponse(template.render(context))
	