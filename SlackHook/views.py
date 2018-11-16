from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import SlackUser, Channel, Message

import datetime


class SlackHookView(TemplateView):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(SlackHookView, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		context = super(SlackHookView, self).get_context_data(**kwargs)
		context['channels'] = Channel.objects.all()
		for channel in context['channels']:
			channel.messages = Message.objects.filter(channel=channel)
		return context


	def get(self, request, *args, **kwargs):
		return self.render_to_response(self.get_context_data())

	def post(self, request, *args, **kwargs):
		self.process_request(request)
		return HttpResponse('Hello')

	def process_request(self, request):
		try:
			token = request.POST['token']
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
				user_id = user_id,
				user_name = user_name
			)[0]
		user.save()
		
		channel = Channel.objects.get_or_create(
				channel_id = channel_id,
				channel_name = channel_name
			)[0]
		channel.save()

		message = Message(
				slack_user = user, 
				channel = channel,
				trigger_word = trigger_word,
				text = text,
				timestamp = timestamp
			)
		message.save()




