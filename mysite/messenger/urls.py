from django.urls import path
from django.views.generic import RedirectView
from .views import index, IndexView
app_name = 'messenger'
urlpatterns = [
    # dossiers
    path('inbox/',index,name='inbox'),
    path('sent/',index,name='sent'),
    # actions
    path('write/',index,name='write'),
    path('view/<int:id>/',index,name='view'),
    path('delete/',index,name='delete'),
    
    # path('',RedirectView.as_view(
    #     pattern_name='messenger:inbox',permanent=True)),
    path('', IndexView.as_view()),
]