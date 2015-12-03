from django.conf.urls import url

urlpatterns = [
    url(r'^signup/', 'accounts.views.signup_step_1_confirm_email', name="signup_step_1_confirm_email"),
    url(r'^await-confirmation/', 'accounts.views.signup_step_2_await_confirmation'),
    url(r'^purchase-ithaca-dollars/', 'accounts.views.purchase_ithaca_dollars'),
    url(r'^create_account/(?P<email_key>\w+)', 'accounts.views.signup_step_3_select_account_type', name="select_account_type"),
    url(r'^account-information/', 'accounts.views.signup_step_4_account_information'),
    url(r'^list_accounts/$', 'accounts.views.list_accounts'),
]
