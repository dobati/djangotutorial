
# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(unique=True, max_length=80)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
# 
# 
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey('AuthPermission')
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
# 
# 
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(max_length=50)
#     content_type = models.ForeignKey('DjangoContentType')
#     codename = models.CharField(max_length=100)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
# 
# 
# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
# 
# 
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
# 
# 
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
# 
# 
# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     action_time = models.DateTimeField()
#     user = models.ForeignKey(AuthUser)
#     content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
# 
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
# 
# 
# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
# 
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
# 
# 
# class DjangoMigrations(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
# 
# 
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'django_session'

# Just in case: 


# class PollsChoice(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField()
#     poll = models.ForeignKey('PollsPoll')
# 
#     class Meta:
#         managed = False
#         db_table = 'polls_choice'
# 
# 
# class PollsPoll(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'polls_poll'
# 
# 
# class SignupsPost(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     author = models.ForeignKey(AuthUser)
#     text = models.TextField()
#     created_date = models.DateTimeField()
#     published_date = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'signups_post'
# 
# 
# class SignupsSignup(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     first_name = models.CharField(max_length=120, blank=True)
#     last_name = models.CharField(max_length=120, blank=True)
#     email = models.CharField(max_length=75)
#     timestamp = models.DateTimeField()
#     updated = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'signups_signup'
# 
# 
# class SignupsUserinput(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     translation = models.TextField(blank=True)
#     timestamp = models.DateTimeField()
#     updated = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'signups_userinput'
# 
# 
# class SouthMigrationhistory(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app_name = models.CharField(max_length=255)
#     migration = models.CharField(max_length=255)
#     applied = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'south_migrationhistory'
# 
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __unicode__(self): 
#         return self.question_text
# 
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __unicode__(self):
#         return self.choice_text
# 
# class TatoebaEnEs(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     source = models.TextField()
#     target = models.TextField()
#     def translation(self):
#         return self.target
#     def __unicode__(self):
#         return self.source
#     class Meta:
#         db_table = 'tatoeba_en_es'

