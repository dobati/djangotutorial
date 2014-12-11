##########################################################################################
#
# PREVIOUS VERSIONS FOR CHECKING AND COMPARING



#random_list = []
# def trans(request, message, dbtable, levelchoice):  
# 	chosen_topic = message
# 	randomchoice =random.choice(dbtable.objects.filter(level=levelchoice))
# 	random_list.append(randomchoice)
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		previous_randomchoice = random_list[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		#form = UserInputForm(request.POST or None)
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': message,
#     					 				'r': previous_randomchoice ,
#                                           'form': form,
#                                           't' :previous_randomchoice.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': message,
#                                    'r': randomchoice,
#   				  					'form': form,
#                                        }) 


#
#lgeneral_1 = []
# def general1(request):  
# 	chosen_topic = "<h1>Your choice: General domain, level 1</h1>"
# 	r_general_1 =random.choice(GeneralEnEs.objects.filter(level=1))
# 	lgeneral_1.append(r_general_1)
# 	form = UserInputForm(request.POST or None)
# 	
# 	# the form is valid as soon as the user writes anything
# 	if form.is_valid():	
# 		# in the meantime another random object has already been created so we have to retrieve the second last one from the list
# 		rr_general_1 = lgeneral_1[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           {
#                                           'chosen_topic': chosen_topic,
#     					 				'r': rr_general_1,
#                                           'form': form,
#                                           't' :rr_general_1.translation(),
# 					  })
# 					  
# 		# this is shown when the user first opens the page, becaus the form (translation) does not exist yet, hence it is not valid yet			  
#        	return render(request, "polls/translate.html",
#        							 { 
#        							 	'chosen_topic': chosen_topic,
#                                    'r': r_general_1 ,
#   				  				'form': form,
#                                        })

# lgeneral_2 = []
# def general2(request):  
# 	chosen_topic = "<h1>Your choice: General domain, level 2</h1>"
# 	r_general_2 =random.choice(GeneralEnEs.objects.filter(level=2))
# 	lgeneral_2.append(r_general_2)
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_general_2 = lgeneral_2[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     					 				'r': rr_general_2,
#                                           'form': form,
#                                           't' :rr_general_2.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_general_2,
#   				  					'form': form,
#                                        }) 

# lgeneral_3 = []
# def general3(request):  
# 	chosen_topic = "<h1>Your choice: General domain, level 3</h1>"  
# 	r_general_3 =random.choice(GeneralEnEs.objects.filter(level=3))
# 	lgeneral_3.append(r_general_3)
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_general_3 = lgeneral_3[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     									 'r': rr_general_3,
#                                           'form': form,
#                                           't' :rr_general_3.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_general_3,
#   				  'form': form,
#                                        })                              
# 		

# lbooks_1 = []
# 
# def books1(request):
# 	chosen_topic = "<h1>Your choice: Books, level 1</h1>" 
# 	r_books_1 =random.choice(ThelittleprinceEnEs.objects.filter(level=1))
# 	lbooks_1.append(r_books_1)    
# 	form = UserInputForm(request.POST or None)
# 	
# 	# if the user writes something and submits, then show me the original translation
# 	if form.is_valid(): 
# 		rr_books_1 = lbooks_1[-2]
# 		
# 		#my_tr_model = UserInput()
# 		#my_tr_model.translation = form.cleaned_data.get('form_translation')
# 		#my_tr_model.save()
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		form = UserInputForm(request.POST or None)
# 		#return http.HttpResponseRedirect('')
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     									 'r': rr_books_1,
#                                           'form': form,
#                                           't' :rr_books_1.translation(),
#                                           
# 										  })
# 	
# 	# when the user goes to the webpage books1, show a random sentence and the box window where the user can write his translation
# 	#if not form.is_valid(): 
# 	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_books_1,
#   								  'form': form,
#                                        })   




# random satz and the message to the user is the only thing that changes

# lbooks_2 = []
# def books2(request):
# 	chosen_topic = "<h1>Your choice: Books, level 2</h1>" 
# 	r_books_2 =random.choice(ThelittleprinceEnEs.objects.filter(level=2))
# 	lbooks_2.append(r_books_2)    
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_books_2 = lbooks_2[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     								 'r': rr_books_2,
#                                           'form': form,
#                                           't' :rr_books_2.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_books_2,
#   				 				 'form': form,
#                                        }) 
# 
# 
# 
# lbooks_3 = []
# def books3(request):
# 	chosen_topic = "<h1>Your choice: Books, level 3</h1>" 
# 	r_books_3 =random.choice(ThelittleprinceEnEs.objects.filter(level=3))
# 	lbooks_3.append(r_books_3)    
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_books_3 = lbooks_3[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     					 				'r': rr_books_3,
#                                           'form': form,
#                                           't' :rr_books_3.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_books_3,
#   				  					'form': form,
#                                        }) 


# lmovies_1 = []
# def movies1(request):  
# 	chosen_topic = "<h1>Your choice: Movies, level 1</h1>" 
# 	r_movies1 =random.choice(SubsEnEs.objects.filter(level=1))
# 	lmovies_1.append(r_movies1) 
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_movies1 = lmovies_1[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     					 				'r': rr_movies1,
#                                           'form': form,
#                                           't' :rr_movies1.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_movies1,
#   				  				'form': form,
#                                        })
# 
# lmovies_2 = []
# def movies2(request):  
# 	chosen_topic = "<h1>Your choice: Books, level 2</h1>" 
# 	r_movies2 =random.choice(SubsEnEs.objects.filter(level=2))
# 	lmovies_2.append(r_movies2) 
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_movies2 = lmovies_2[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#     					'chosen_topic': chosen_topic,
#     					 'r': rr_movies2,
#                                           'form': form,
#                                           't' :rr_movies2.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_movies2,
#   				  'form': form,
#                                        })
# 
#  
# lmovies_3 = []
# def movies3(request): 
# 	chosen_topic = "<h1>Your choice: Books, level 3</h1>"  
# 	r_movies3 =random.choice(SubsEnEs.objects.filter(level=3))
# 	lmovies_3.append(r_movies3) 
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_movies3 = lmovies_3[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#     					 		'chosen_topic': chosen_topic,
#     					 		'r': rr_movies3,
#                                           'form': form,
#                                           't' :rr_movies3.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 
#                                    'chosen_topic': chosen_topic,
#                                    'r': r_movies3,
#   				  				'form': form,
#                                        })
#                                        
# 
# llegal_1 = [] 
# def legaltexts1(request):
# 	chosen_topic = "<h1>Your choice: Legal Texts, level 1</h1>" 
# 	r_legaltexts1 = random.choice(EuconstEnEs.objects.filter(level=1))
# 	llegal_1.append(r_legaltexts1)
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_legaltexts1 = llegal_1[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		
# 		return render(request, "polls/translate.html",
#                                           { 
#                                           'chosen_topic': chosen_topic,
#     					 'r': rr_legaltexts1,
#                                           'form': form,
#                                           't' :rr_legaltexts1.translation(),
# 					  })
# 		
# 	
#     	return render(request, "polls/translate.html",
#                                    { 'chosen_topic': chosen_topic,
#                                    'r': r_legaltexts1,
#   				  'form': form,
#                                      })
# 	
# 
# 
# llegal_2 = []
# def legaltexts2(request):  
# 	chosen_topic = "<h1>Your choice: Legal Texts, level 2</h1>" 
# 	r_legaltexts2 = random.choice(EuconstEnEs.objects.filter(level=2))  
# 	llegal_2.append(r_legaltexts2)
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_legaltexts2 = llegal_2[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           { 
#     					 'chosen_topic': chosen_topic,
#     					 'r': rr_legaltexts2,
#                                           'form': form,
#                                           't' :rr_legaltexts2.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 'chosen_topic': chosen_topic,
#                                    'r': r_legaltexts2,
#   				  'form': form,
#                                      })
# 
# 
# llegal_3 = []
# def legaltexts3(request):
# 	chosen_topic = "<h1>Your choice: Legal Texts, level 3</h1>" 
# 	r_legaltexts3 =random.choice(EuconstEnEs.objects.filter(level=3))
# 	llegal_3.append(r_legaltexts3)    
# 	form = UserInputForm(request.POST or None)
# 	if form.is_valid():
# 		rr_legaltexts3 = llegal_3[-2]
# 		save_it = form.save(commit=False)
# 		save_it.save()
# 		return render(request, "polls/translate.html",
#                                           {
#                                           'chosen_topic': chosen_topic, 
#     					 'r': rr_legaltexts3,
#                                           'form': form,
#                                           't' :rr_legaltexts3.translation(),
# 					  })
#        	return render(request, "polls/translate.html",
#                                    { 'chosen_topic': chosen_topic,
#                                    'r': r_legaltexts3,
#   				  'form': form,
#                                      })
##########################################################################################
#
# FIRST TRY: SIMPLIEST VERSION
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

