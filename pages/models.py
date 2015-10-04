from django.contrib.flatpages.models import FlatPage
from django.db import models


class SubPage(models.Model):
    flatpage = models.OneToOneField(FlatPage, primary_key=True, related_name='subpage', blank=True)
    heading = models.CharField(max_length=100)
    meta_desc = models.TextField(blank=True, default="Ithacash is a regional benefit currency for Ithaca and Tompkins County. Every Ithaca Dollar spent becomes an immediate buy-local success. There's no catch. It's money that stays in our region by design, strengthening our local economy and meeting our community's needs, period.")
    meta_keywords = models.TextField(blank=True, default='ithaca, local, currency')


class UploadedFiles(models.Model):
    file = models.FileField()
