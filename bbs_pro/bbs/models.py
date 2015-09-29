from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BBS(models.Model):
	title = models.CharField(max_length = 64)
	categray = models.ForeignKey('Categray')
	summary = models.CharField(max_length = 256,blank = True,null=True)
	content = models.TextField()
	author = models.ForeignKey('BBS_user')
	view_count = models.IntegerField()
	ranking = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add= True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-created_at']


class Categray(models.Model):
	name = models.CharField(max_length=32,unique=True)
	administrator = models.ForeignKey('BBS_user')

	def __unicode__(self):
		return self.name

class BBS_user(models.Model):
	user = models.OneToOneField(User)
	signature = models.CharField(max_length=128,default='The gay is too lazy to leave anything!!')
	photo = models.ImageField(upload_to="photo/",default="photo/default.jpg")
	def __unicode__(self):
		return self.user.username

class Chat(models.Model):
	content = models.CharField(max_length=300)
	author = models.ForeignKey(User)
	submit_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content
	class Meta:
		ordering = ['-submit_at']
