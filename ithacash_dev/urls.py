from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

'''
Are you adding a new app?

Currently our caching service (Varnish) strips all cookies
unless they are from a whitelisted URL path.

This is suggested by the Varnish documentation for websites
which only use CSRF on certain URL paths.

https://www.varnish-cache.org/docs/4.0/users-guide/increasing-your-hitrate.html#cookies-from-the-client

If your new app is not read-only (and needs the CSRF cookie), add it to the
whitelisted URLs here:

See ops/ansible/playbooks/roles/caching/templates/etc__varnish__default.vcl
'''


def error_view(request):
    raise RuntimeError("This is a test Ithacash error.")

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.front'),
    url(r'^apply/$', RedirectView.as_view(url='/accounts/signup/')),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^paypal_ipn_endpoint/', 'payments.views.paypal_ipn_endpoint', name="paypal_ipn_endpoint"),
    url(r'^thanks/$', 'accounts.views.thanks'),
    url(r'^whoops/$', 'accounts.views.whoops'),
    url(r'^everyone/$', 'pages.views.everyone'),
    url(r'^test_utils/error_test/$', error_view)
]
