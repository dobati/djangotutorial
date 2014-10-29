from django.shortcuts import redirect 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import TatoebaEnEs
from django.template import RequestContext, loader
import random
from .forms import UserInputForm

# Create your views here


def index(request):
    return render_to_response("polls/index.html",
                              context_instance = RequestContext(request))



r = TatoebaEnEs.objects.all().order_by('?')[0]
t = r.translation()


def books1(request):
	#r = TatoebaEnEs.objects.all().order_by('?')[0]
	#t = r.translation()
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/books1.html",
                                          { 
    					 'r': r,
                                          'form': form,
                                          't' :t,
					  })
        return render(request, "polls/books1.html",
                                   { 'r': r,
  				  'form': form,
                                       })
                                       
		
                                          


def books2(request):
    return render_to_response("polls/books2.html",
                              context_instance = RequestContext(request))
def books3(request):
    return render_to_response("polls/books3.html",
                              context_instance = RequestContext(request))

def movies1(request):
    return render_to_response("polls/movies1.html",
                              context_instance = RequestContext(request))
def movies2(request):
    return render_to_response("polls/movies2.html",
                              context_instance = RequestContext(request))
def movies3(request):
    return render_to_response("polls/movies3.html",
                              context_instance = RequestContext(request))

def legaltexts1(request):
    return render_to_response("polls/legaltexts1.html",
                              context_instance = RequestContext(request))
def legaltexts2(request):
    return render_to_response("polls/legaltexts2.html",
                              context_instance = RequestContext(request))
def legaltexts3(request):
    return render_to_response("polls/legaltexts3.html",
                              context_instance = RequestContext(request))
