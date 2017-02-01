from django.conf.urls import url
from . import views

app_name = 'Tennis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<player_id>[0-9]+)$', views.player_profile, name='player_profile'),
    ]
