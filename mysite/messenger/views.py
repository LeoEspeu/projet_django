import os

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import RedirectView
import logging
from .models import Message

logger = logging.getLogger('messenger.views')

# Create your views here.
def index(request):
    demo = list(Message.objects.all()) # démo middleware
    demo = Message.objects.only('body').get(pk=2) # démo
    #logger.debug('message de démonstration')
    return render(request, 'messenger/index.html')

class IndexView(RedirectView):
    pattern_name = 'messenger:inbox'
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.pattern_name,
                       args=args,kwargs=kwargs,
                       current_app=self.request.resolver_match.namespace)


class AjaxUnreadCountView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = {'unread_count': Message.objects.filter(
                recipient = request.user,
                read_at__isnull=True,
                recipient_deleted_at__isnull=True).count()}
        else:
            data = {}
        return JsonResponse(data)