from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from ithacash.views import StaticViewSitemap, SubpagesSitemap

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


sitemaps = {'front': StaticViewSitemap, 'subpages': SubpagesSitemap}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.front', name='front'),
    url(r'^robots.txt', 'ithacash.views.robots_txt'),
    url(r'^apply/$', RedirectView.as_view(url='/accounts/signup/', permanent=False)),
    url(r'^join/$', RedirectView.as_view(url='/accounts/signup/', permanent=False), name='join'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^paypal_ipn_endpoint/', 'payments.views.paypal_ipn_endpoint', name="paypal_ipn_endpoint"),
    url(r'^thanks/$', 'accounts.views.thanks'),
    url(r'^whoops/$', 'accounts.views.whoops'),
    url(r'^test_utils/error_test/$', error_view),
    url(r'^page-creator/$', 'pages.views.page_creator'),
    url(r'^page-creator/files/$', 'pages.views.files'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('django.contrib.flatpages.urls')),
]
