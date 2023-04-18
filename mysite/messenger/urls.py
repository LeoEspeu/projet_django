from django.urls import path
from django.views.generic import RedirectView, TemplateView
from .views import index, IndexView
from .views import AjaxUnreadCountView # démo AJAX
app_name = 'messenger'
urlpatterns = [
    # dossiers
    path('inbox/',index,name='inbox'),
    path('sent/',index,name='sent'),
    # actions
    path('write/',index,name='write'),
    path('view/<int:id>/',index,name='view'),
    path('delete/',index,name='delete'),
    path('light',TemplateView.as_view(
        template_name='index.html',
        template_engine='django_light'
    )),
    path('unread-count/', AjaxUnreadCountView.as_view()),
    # path('',RedirectView.as_view(
    #     pattern_name='messenger:inbox',permanent=True)),
    path('', IndexView.as_view()),
]