from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'accounts.views.getting_an_account'),
    url(r'^signup/', 'accounts.views.signup_phase_one', name="signup_phase_one"),
    url(r'^await-confirmation/', 'accounts.views.await_confirmation'),
    url(r'^purchase-ithaca-dollars/', 'accounts.views.purchase_ithaca_dollars'),
    url(r'^create_account/(?P<email_key>\w+)', 'accounts.views.create_account', name="account_application"),
    url(r'^review/$', 'accounts.views.review'),
    url(r'^list_accounts/$', 'accounts.views.list_accounts'),
    ]
