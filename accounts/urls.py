from django.conf.urls import url

urlpatterns = [
    url(r'^signup/', 'accounts.views.signup_phase_one'),
    ]