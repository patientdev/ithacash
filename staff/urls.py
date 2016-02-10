from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^$', views.staff_front),
    url(r'^login/', views.login_staff),
    url(r'^signup/', views.signup),
    url(r'^dashboard/', views.dashboard),
    url(r'^api/search-users/', api.search_users),
    url(r'^api/confirm-staff/(?P<confirmation_key>\w+)', api.confirm_staff)
]
