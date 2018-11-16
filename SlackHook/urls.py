from django.urls import path, include

from .views import SlackHookView

urlpatterns = [
    path('', SlackHookView.as_view(template_name='SlackHook/display_hooks.html'), name='slack_hook'),
]
