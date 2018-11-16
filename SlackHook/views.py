from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class SlackHookView(TemplateView):
	
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(SlackHookView, self).dispatch(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		self.process_request(request)
		return HttpResponse('Hello')

	def process_request(self, request):
		try:
			token = request.POST.get['token']
			team_domain = request.POST.get['team_domain']
			channel_name = request.POST.get['channel_name']
			timestamp = request.POST.get['timestamp']
			user_name = request.POST.get['user_name']
			text = request.POST.get['text']
			trigger_word = request.POST.get['trigger_word']
		except KeyError:
			return
		

