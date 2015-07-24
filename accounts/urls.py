from django.conf.urls import url

urlpatterns = [
    url(r'^signup/', 'accounts.views.signup_phase_one'),
    url(r'^create_account/(?P<email_key>\w+)', 'accounts.views.create_account'),
    url(r'^list_accounts/$', 'accounts.views.list_accounts'),
    ]