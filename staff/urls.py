from django.conf.urls import url

urlpatterns = [
    url(r'^login/', 'staff.views.login'),
    url(r'^signup/', 'staff.views.signup'),
]
