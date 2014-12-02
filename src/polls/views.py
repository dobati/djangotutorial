# views.py

# Imports
# ========================================================================================

# To be able to render a page when you click on it
from django.shortcuts import render

# import render_to_response and RequestContext for index and about us page (check the difference of django.shortcuts)
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

# import Tables Models for all domain
from .models import GeneralEnEs
from .models import SubsEnEs
from .models import EuconstEnEs
from .models import ThelittleprinceEnEs

# import model for the user input - translation
from .models import UserInput

# import form for the user input - translation
from .forms import UserInputForm

# for choosing random input from the database
import random

# for spell checking
#import aspell

# for handling punctuation marks and regex
import string, re

# if we want to make the random faster, we should define our own random function (if you have time)
#from .models import Random

#import Levenshtein as lev
import functions
from .functions import compare
from .functions import spelling_checker



# Views for the index and about us pages
# ========================================================================================

# View for the main page:
def index(request):
    return render_to_response("polls/index.html",
                              context_instance = RequestContext(request))
                              
# View for the page about us                           
def aboutus(request):
    return render_to_response("polls/aboutus.html",
                              context_instance = RequestContext(request))
                              

# Views for the pages where the user is asked to enter user input
# ========================================================================================

def general1(request):
	return trans(request, "Your choice: General domain, level 1", GeneralEnEs, 1)
	
def general2(request):
	return trans(request, "Your choice: General domain, level 2", GeneralEnEs, 2)
	
def general3(request):
	return trans(request, "Your choice: General domain, level 3", GeneralEnEs, 3)


def books1(request):
	return trans(request, "Your choice: Books, level 1", ThelittleprinceEnEs, 1)
	
def books2(request):
	return trans(request, "Your choice: Books, level 2", ThelittleprinceEnEs, 2)
	
def books3(request):
	return trans(request, "Your choice: Books, level 3", ThelittleprinceEnEs, 3)
	
	
def movies1(request):  
	return trans(request, "Your choice: Movies, level 1", SubsEnEs, 1)

def movies2(request):  
	return trans(request, "Your choice: Movies, level 1", SubsEnEs, 2)

def movies3(request):  
	return trans(request, "Your choice: Movies, level 1", SubsEnEs, 3)
	
	
def legaltexts1(request):
	return trans(request,  "Your choice: Legal Texts, level 1", EuconstEnEs, 1)

def legaltexts2(request):
	return trans(request,  "Your choice: Legal Texts, level 2", EuconstEnEs, 2)
	
def legaltexts3(request):
	return trans(request,  "Your choice: Legal Texts, level 3", EuconstEnEs, 3)


                

# Function trans() : main view
# ========================================================================================

random_list = []
def trans(request, message, dbtable, levelchoice):  

	"""Main function: takes the user input and returns the reference translation
	after the user submits the input"""
	
	chosen_topic = message
	your_translation = 'Your translation:'
	reference_translation = 'Reference translation:'
	randomchoice =random.choice(dbtable.objects.filter(level=levelchoice))
	random_list.append(randomchoice)
	
	form = UserInputForm(request.POST or None)
	if form.is_valid():
		userinputmodel = UserInput()
		
		userinputmodel.translation = form.cleaned_data.get('form_translation')
		previous_randomchoice = random_list[-2]		
		saved_trans = userinputmodel.translation #.save() we cannot save unicode objects!	
		spelling_checker(saved_trans)
		
		
		evaluate_user = compare(previous_randomchoice.translation(), saved_trans)
							
		return render(request, "polls/translate.html",
                                          { 
                                          'chosen_topic': message,
    					 				  'r': previous_randomchoice ,
                                          'form': form,
                                          'your_translation': your_translation, 
                                          'saved_tr':functions.saved_tr, # we are importing the variable saved_tr from the module functions
                                          'reference_translation': reference_translation,
                                          't' :previous_randomchoice.translation(),
                                          'evaluate_user': evaluate_user,

					  })
       	return render(request, "polls/translate.html",
                                   { 
                                   'chosen_topic': message,
                                   'r': randomchoice,
  				  					'form': form,
                                       }) 



        
# TO DO:
# 1. since the orderby ? was faster, think again if you want to use it instead of random.choice
# 2. Get rid of the error message - This field is required.
# CSS:

#myDIV {
#    text-decoration: underline;
#    text-decoration-color:red;
#}
