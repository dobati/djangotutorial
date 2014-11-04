from django.shortcuts import redirect 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import GeneralEnEs
from .models import SubsEnEs
from .models import EuconstEnEs
from .models import ThelittleprinceEnEs
from django.template import RequestContext, loader
import random
from .forms import UserInputForm

# Create your views here


def index(request):
    return render_to_response("polls/index.html",
                              context_instance = RequestContext(request))



lgeneral_1 = []
def general1(request):    
	r_general_1 =random.choice(GeneralEnEs.objects.filter(level=1))
	lgeneral_1.append(r_general_1)
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_general_1 = lgeneral_1[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/general1.html",
                                          { 
    					 'r': rr_general_1,
                                          'form': form,
                                          't' :rr_general_1.translation(),
					  })
       	return render(request, "polls/general1.html",
                                   { 'r': r_general_1,
  				  'form': form,
                                       })

lgeneral_2 = []
def general2(request):    
	r_general_2 =random.choice(GeneralEnEs.objects.filter(level=2))
	lgeneral_2.append(r_general_2)
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_general_2 = lgeneral_2[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/general2.html",
                                          { 
    					 'r': rr_general_2,
                                          'form': form,
                                          't' :rr_general_2.translation(),
					  })
       	return render(request, "polls/general2.html",
                                   { 'r': r_general_2,
  				  'form': form,
                                       }) 


lgeneral_3 = []
def general3(request):    
	r_general_3 =random.choice(GeneralEnEs.objects.filter(level=3))
	lgeneral_3.append(r_general_3)
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_general_3 = lgeneral_3[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/general3.html",
                                          { 
    					 'r': rr_general_3,
                                          'form': form,
                                          't' :rr_general_3.translation(),
					  })
       	return render(request, "polls/general3.html",
                                   { 'r': r_general_3,
  				  'form': form,
                                       })                              
		
 
lbooks_1 = []
def books1(request):
	r_books_1 =random.choice(ThelittleprinceEnEs.objects.filter(level=1))
	lbooks_1.append(r_books1)    
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_books_1 = lbooks_1[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/books1.html",
                                          { 
    					 'r': rr_books_1,
                                          'form': form,
                                          't' :rr_books_1.translation(),
					  })
       	return render(request, "polls/books1.html",
                                   { 'r': r_books_1,
  				  'form': form,
                                       })   

lbooks_2 = []
def books2(request):
	r_books_2 =random.choice(ThelittleprinceEnEs.objects.filter(level=2))
	lbooks_2.append(r_books2)    
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_books_2 = lbooks_2[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/books2.html",
                                          { 
    					 'r': rr_books_2,
                                          'form': form,
                                          't' :rr_books_2.translation(),
					  })
       	return render(request, "polls/books2.html",
                                   { 'r': r_books_2,
  				  'form': form,
                                       }) 



lbooks_3 = []
def books3(request):
	r_books_3 =random.choice(ThelittleprinceEnEs.objects.filter(level=3))
	lbooks_3.append(r_books3)    
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_books_3 = lbooks_3[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/books3.html",
                                          { 
    					 'r': rr_books_3,
                                          'form': form,
                                          't' :rr_books_3.translation(),
					  })
       	return render(request, "polls/books3.html",
                                   { 'r': r_books_3,
  				  'form': form,
                                       }) 


lmovies_1 = []
def movies1(request):  
	r_movies1 =random.choice(SubsEnEs.objects.filter(level=1))
	lmovies_1.append(r_movies1) 
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_movies1 = lmovies_1[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/movies1.html",
                                          { 
    					 'r': rr_movies1,
                                          'form': form,
                                          't' :rr_movies1.translation(),
					  })
       	return render(request, "polls/movies1.html",
                                   { 'r': r_movies1,
  				  'form': form,
                                       })

lmovies_2 = []
def movies2(request):  
	r_movies2 =random.choice(SubsEnEs.objects.filter(level=2))
	lmovies_2.append(r_movies2) 
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_movies2 = lmovies_2[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/movies2.html",
                                          { 
    					 'r': rr_movies2,
                                          'form': form,
                                          't' :rr_movies2.translation(),
					  })
       	return render(request, "polls/movies2.html",
                                   { 'r': r_movies2,
  				  'form': form,
                                       })

 
lmovies_3 = []
def movies3(request):  
	r_movies3 =random.choice(SubsEnEs.objects.filter(level=3))
	lmovies_3.append(r_movies3) 
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_movies3 = lmovies_3[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/movies3.html",
                                          { 
    					 'r': rr_movies3,
                                          'form': form,
                                          't' :rr_movies3.translation(),
					  })
       	return render(request, "polls/movies3.html",
                                   { 'r': r_movies3,
  				  'form': form,
                                       })
                                       

llegal_1 = [] 
def legaltexts1(request):
	r_legaltexts1 = random.choice(EuconstEnEs.objects.filter(level=1))
	llegal_1.append(r_legaltexts1)
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_legaltexts1 = llegal_1[-2]
		save_it = form.save(commit=False)
		save_it.save()
		
		return render(request, "polls/legaltexts1.html",
                                          { 
    					 'r': rr_legaltexts1,
                                          'form': form,
                                          't' :rr_legaltexts1.translation(),
					  })
		
	
    	return render(request, "polls/legaltexts1.html",
                                   { 'r': r_legaltexts1,
  				  'form': form,
                                     })
	


llegal_2 = []
def legaltexts2(request):  
	r_legaltexts2 = random.choice(EuconstEnEs.objects.filter(level=2))  
	llegal_2.append(r_legaltexts2)
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_legaltexts2 = llegal_2[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/legaltexts2.html",
                                          { 
    					 'r': rr_legaltexts2,
                                          'form': form,
                                          't' :rr_legaltexts2.translation(),
					  })
       	return render(request, "polls/legaltexts2.html",
                                   { 'r': r_legaltexts2,
  				  'form': form,
                                     })


llegal_3 = []
def legaltexts3(request):
	r_legaltexts3 =random.choice(EuconstEnEs.objects.filter(level=3))
	llegal_3.append(r_legaltexts3)    
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		rr_legaltexts3 = llegal_3[-2]
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "polls/legaltexts3.html",
                                          { 
    					 'r': rr_legaltexts3,
                                          'form': form,
                                          't' :rr_legaltexts3.translation(),
					  })
       	return render(request, "polls/legaltexts3.html",
                                   { 'r': r_legaltexts3,
  				  'form': form,
                                     })

# How it was before:
#                                                                    
# def books2(request):
#     return render_to_response("polls/books2.html",
#                               context_instance = RequestContext(request))
# def books3(request):
#     return render_to_response("polls/books3.html",
#                               context_instance = RequestContext(request))
# def movies1(request):
#     return render_to_response("polls/movies1.html",
#                               context_instance = RequestContext(request))
# def movies2(request):
#     return render_to_response("polls/movies2.html",
#                               context_instance = RequestContext(request))
# def movies3(request):
#     return render_to_response("polls/movies3.html",
#                               context_instance = RequestContext(request))
# 
# def legaltexts1(request):
#     return render_to_response("polls/legaltexts1.html",
#                               context_instance = RequestContext(request))
# def legaltexts2(request):
#     return render_to_response("polls/legaltexts2.html",
#                               context_instance = RequestContext(request))
# def legaltexts3(request):
#     return render_to_response("polls/legaltexts3.html",
#                               context_instance = RequestContext(request))
