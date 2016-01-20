from django.conf.urls import url

urlpatterns = [
    url(r'^login/', 'staff.views.login_staff'),
    url(r'^signup/', 'staff.views.signup'),
    url(r'^(?P<staff_id>\d*)', 'staff.views.dashboard'),
]
