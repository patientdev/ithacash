from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from datetime import datetime


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['front', 'signup_phase_one']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return datetime.now()


class SubpagesSitemap(FlatPageSitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return FlatPage.objects.all()

    def lastmod(self, item):
        return datetime.now()


def robots_txt(request):
    return render(request, 'robots.txt', content_type="text/plain")
