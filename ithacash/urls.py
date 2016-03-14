from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
import pages, ithacash, accounts
from ithacash.views import StaticViewSitemap, SubpagesSitemap

from ithacash import views as main_views
from pages import views as subpage_views
from accounts import views as account_views
from payments import views as payment_views
from django import views as django_views
from django.template import Context, loader
from django.http import HttpResponseServerError, HttpResponseNotFound


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


# Serve errors using a template so it looks nice and is somewhat helpful
def handler404(request):
    t = loader.get_template('404.html')
    return HttpResponseNotFound(t.render(Context({
        'request': request,
    })))


def handler500(request):
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


sitemaps = {'front': StaticViewSitemap, 'subpages': SubpagesSitemap}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', subpage_views.front, name='front'),
    url(r'^robots.txt', main_views.robots_txt),
    url(r'^apply/$', RedirectView.as_view(url='/accounts/signup/', permanent=False)),
    url(r'^join/$', RedirectView.as_view(url='/accounts/signup/', permanent=False), name='join'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^staff/', include('staff.urls')),
    url(r'^pages/', include('pages.urls')),

    url(r'^paypal_ipn_endpoint/', payment_views.paypal_ipn_endpoint, name="paypal_ipn_endpoint"),
    url(r'^whoops/$', account_views.whoops),
    url(r'^test_utils/error_test/$', error_view),
    url(r'^test_utils/500_test/$', handler500),
    url(r'^test_utils/404_test/$', handler404),
    url(r'^media/(?P<path>.*)$', django_views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('django.contrib.flatpages.urls')),
]
