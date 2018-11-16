from django.db import models
from django.utils.timesince import timesince


class SlackUser(models.Model):
	"""
	Class representing Slack User
	"""
	user_id 		= models.CharField(max_length=255, unique=True)
	user_name 		= models.CharField(max_length=255)


class Channel(models.Model):
	"""
	Class representing Slack Channel
	"""
	channel_id 		= models.CharField(max_length=255, unique=True)
	channel_name 	= models.CharField(max_length=255)


class Message(models.Model):
	"""
	Class representing Slack Message
	"""
	slack_user 		= models.ForeignKey(SlackUser, on_delete=models.CASCADE)
	channel 		= models.ForeignKey(Channel, on_delete=models.CASCADE)
	trigger_word 	= models.CharField(max_length=255)
	text 			= models.TextField(null=True)
	timestamp 		= models.DateTimeField()

	@property
	def age(self):
		age = timesince(self.timestamp)
		if age == '0 minutes':
			age = 'Now'
		return "{t} ago".format(t=age)

	def __str__(self):
		return self.text
