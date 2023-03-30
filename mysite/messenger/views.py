from django.shortcuts import render
from django.urls import reverse
from django.views.generic import RedirectView

# Create your views here.
def index(request):
    return render(request, 'messenger/index.html')

class IndexView(RedirectView):
    pattern_name = 'messenger:inbox'
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.pattern_name,
                       args=args,kwargs=kwargs,
                       current_app=self.request.resolver_match.namespace)