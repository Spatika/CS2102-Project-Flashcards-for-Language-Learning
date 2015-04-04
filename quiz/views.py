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