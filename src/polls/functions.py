# -*- coding: utf-8 -*-
import random
import re
import string
import Levenshtein as lev
import aspell
import string, re


# Function spelling_checker
# ========================================================================================

def spelling_checker(inputsentence):

	""" function for checking the spelling of each word in users sentence and 
	 underlining it (possibly with CSS) its spelled wrongly"""
	 
	spelling = aspell.Speller('lang', 'es')
	global saved_tr
	saved_tr = str(inputsentence)
	
	#replacing the punctuation marks from the input because the spelling checker doesn't do that automatically
	replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
	saved_tr = saved_tr.translate(replace_punctuation)	
		
	saved_tr = saved_tr.split()
	spelled_list = []
	for word in saved_tr:	
		checked_spelling = spelling.check(word)
		if checked_spelling != 1:
			word = "<p class='highlight'>"+word+"</p>"  				#'underline the false pronounced word (save_it) in the translation'
			spelled_list.append(word)
		else:
			spelled_list.append(word)
	saved_tr = ' '.join(spelled_list)
	return saved_tr




# Function compare()
# ========================================================================================

def compare(targettrans, usertrans):
    
    '''Takes the target translation and the user translation as inputs.
    Based on their edit distance returns an evaluation.
    @ targettrans: target translation (ideal translation of a text)
    @ usertrans: translation provided by the user '''
    
    evaluation = {'very good': ['Superb translation!', 'Great work!'], \
                  'good': ['Good translation!', \
                            'Nice work!'], \
                  'fair': ['You can do better!', 'Shall we practice a little more?']
                  }
    
    #encode from latin-1 because of python unicode problems!
    
    tt = targettrans.encode('latin-1') #'ascii' codec can't encode character u'\xed' in position 12: ordinal not in range(128)
    
    #try:
    #ut = usertrans.decode("ascii", "ignore")
    
    #----------------- ENCODING PROBLEM---------------------------------------------------
    #   
    ut = str(usertrans) 
    #
    # Wenn der user einen Sonderzeichen schreibet, bekomme ich den Error:
    #
    # 'ascii' codec can't encode character u'\xe1' in position 14: ordinal not in range(128)
    #
    # Wenn ich schreibe:
    #
    # ut = usertrans.encode('latin-1')
    #
    # bekomme ich trotzdem Fehlermeldungen, obwohl es für tt = targettrans.encode('latin-1')  funkioniert!
   
	#----------------- ENCODING PROBLEM---------------------------------------------------
 
    
	# ignore the punctuation in both translation so that Levenstein ratio is 1 
	# when user translation is "No" and reference is "NO!"
    
    replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    
    tt = tt.translate(replace_punctuation).lower()	
    ut = ut.translate(replace_punctuation).lower()
    	
    ratio = lev.ratio(tt, ut) 
    
    if ratio > 0.95:
        return random.choice(evaluation['very good'])
    elif ratio > 0.80:
        return random.choice(evaluation['good'])
    else:
        return random.choice(evaluation['fair'])
        

# Function help()  
# ========================================================================================
        
# words which will be in HELP Window:
        
# def give_clue(targettrans, mttrans):
#     
#     '''Takes two strings as an input and returns a list of unique words.
#     @ targettrans: target translation
#     @ mttrans: machine translation '''
#     
#     pattern = re.compile(r'[^a-zA-Z0-9 \-]')
#     tt = pattern.sub('', targettrans.lower())
#     mt = pattern.sub('', mttrans.lower())
#     words = mt.split() + tt.split()
#     return list(set(words))


#print give_clue('Let it! b-e.', 'let: it snow;')





