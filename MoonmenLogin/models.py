from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30,unique = True,primary_key=True)
	usertype = models.CharField(max_length=10)
	userAvatarUrl = models.URLField()
	createdDate = models.CharField(max_length=10)
	
	def __str__(self):
		return self.username 
class SaveCounterAdvanced(models.Model):
	"""For counting the saved user"""
	uniqueId = models.IntegerField(default=1)
	saveCount = models.IntegerField(default=0)
		