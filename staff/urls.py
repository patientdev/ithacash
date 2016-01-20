from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^login/', views.login_staff),
    url(r'^signup/', views.signup),
    url(r'^(?P<staff_id>\d*)/', views.dashboard),
    url(r'^api/search-users/', api.search_users),
]
