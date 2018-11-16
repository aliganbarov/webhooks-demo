from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from .models import SlackUser, Channel, Message

import datetime


class SlackHookView(TemplateView):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		"""Enables requests from slack's API
		:param request: request data
		:param args:
		:param kwargs:
		:return:
		"""
		return super(SlackHookView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		"""Appends channels and each channels' messages to context
		:param kwargs:
		:return:
		"""
		context = super(SlackHookView, self).get_context_data(**kwargs)
		context['channels'] = Channel.objects.all()
		for channel in context['channels']:
			channel.messages = Message.objects.filter(channel=channel)
		return context

	def get(self, request, *args, **kwargs):
		"""Processes get request to the page
		:param request: request data
		:param args:
		:param kwargs:
		:return: render page with context variable
		"""
		return self.render_to_response(self.get_context_data())

	def post(self, request, *args, **kwargs):
		"""Processes post request to page
		:param request: request data
		:param args:
		:param kwargs:
		:return: redirect to the slack hooks page
		"""
		self.process_request(request)
		return HttpResponseRedirect('/slack_hooks/')

	def process_request(self, request):
		"""Validates request and stores message. Users and channels are created if weren't existing before
		:param request: request data
		:return:
		"""
		try:
			token = request.POST['token']
			if token != 'DKLvgnHZobd6kg3aPbpcohLf':
				return
			channel_id = request.POST['channel_id']
			channel_name = request.POST['channel_name']
			timestamp = datetime.datetime.fromtimestamp(float(request.POST['timestamp']))
			user_id = request.POST['user_id']
			user_name = request.POST['user_name']
			text = request.POST['text']
			trigger_word = request.POST['trigger_word']
		except KeyError:
			return

		user = SlackUser.objects.get_or_create(
				user_id=user_id,
				user_name=user_name
			)[0]
		user.save()
		
		channel = Channel.objects.get_or_create(
				channel_id=channel_id,
				channel_name=channel_name
			)[0]
		channel.save()

		message = Message(
				slack_user=user,
				channel=channel,
				trigger_word=trigger_word,
				text=text,
				timestamp=timestamp
			)
		message.save()
