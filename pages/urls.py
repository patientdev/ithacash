from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page-creator/$', views.page_creator),
    url(r'^page-creator/files/', views.files),
]
