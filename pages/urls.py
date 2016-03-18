from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^page-creator/$', views.page_creator),
    url(r'^page-creator/files/$', views.files),
    url(r'^api/add-to-mailing-list/$', api.add_to_mailing_list),
]
