# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models


# 
class GeneralEnEs(models.Model):
     id = models.IntegerField(primary_key=True)  # AutoField?
     source = models.TextField()
     target = models.TextField()
     level = models.IntegerField()
     entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
     def translation(self):
     	return self.target
     def __unicode__(self):
     	return self.source 
     def niveau(self):
     	return self.level
     class Meta:
         db_table = 'general_en_es'


class SubsEnEs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source = models.TextField()
    target = models.TextField()
    level = models.IntegerField()
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    def translation(self):
	return self.target
    def __unicode__(self):
	return self.source
    def niveau(self):
	return self.level
    class Meta:
        db_table = 'subs_en_es'


class EuconstEnEs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source = models.TextField()
    target = models.TextField()
    level = models.IntegerField()
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    def translation(self):
	return self.target
    def __unicode__(self):
	return self.source
    def niveau(self):
	return self.level
    class Meta:
        db_table = 'euconst_en_es'
        
        
class ThelittleprinceEnEs(models.Model):
    id = models.IntegerField(primary_key=True)  
    source = models.TextField()
    target = models.TextField()
    level = models.IntegerField()
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.   
    def translation(self):
	return self.target
    def __unicode__(self):
	return self.source 
    def niveau(self):
     	return self.level
    class Meta:
        db_table = 'thelittleprince_en_es'
        


class UserInput(models.Model):
	# blank=False because the user input must be empty when we reload the page. 
	# unfortunately I can't get rid of the error message "This field is required." by reloading the page
    
    translation = models.CharField(max_length=120, blank=False) 
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return smart_unicode(self.translation)
    class Meta:
        db_table = 'userinput'


#bis hier
##########################################################################################

# if you have time to implement other random function

# class Random(models.Manager):
#     def random(db):
#         count = db.aggregate(count=Count('id'))['count']
#         random_index = randint(0, count - 1)
#         return db.all()[random_index]

