from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login_staff),
    url(r'^signup/', views.signup),
    url(r'^(?P<staff_id>\d*)', views.dashboard),
]
