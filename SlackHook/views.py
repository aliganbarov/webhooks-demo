from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class SlackHookView(TemplateView):
	
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(SlackHookView, self).dispatch(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		print(request)
		return self.render_to_response('Got a new message!')