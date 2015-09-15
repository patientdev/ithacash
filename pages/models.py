from django.contrib.flatpages.models import FlatPage
from django.db import models


class SubPage(models.Model):
    flatpage = models.OneToOneField(FlatPage, primary_key=True, related_name='subpage', blank=True)
    heading = models.CharField(max_length=100)
