from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Q
from quiz.models import *
# from django.utils import simplejson

# def index(request):
# 	template = loader.get_template('quiz/index.html')
# 	context = RequestContext(request, {})
# 	return HttpResponse(template.render(context))

def index(request):
	# decode_json = simplejson.loads(request.body)
	decode_json = 'French'
	sets = Set.objects.get(
		Q(title__contains=decode_json)|
		Q(description__contains=decode_json)|
		Q(language_from__name__contains=decode_json)|
		Q(language_to__name__contains=decode_json)
		)
	print(sets)
	context = {'Sets':sets}
	return HttpResponse(template.render(context))
	