from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/', views.signup_step_1_confirm_email, name="signup_step_1_confirm_email"),
    url(r'^await-confirmation/', views.signup_step_2_await_confirmation),
    url(r'^purchase-ithaca-dollars/', views.purchase_ithaca_dollars),
    url(r'^create_account/(?P<email_key>\w+)', views.signup_step_3_select_account_type, name="select_account_type"),
    url(r'^account-information/', views.signup_step_4_account_information),
    url(r'^review/$', views.review),
]
