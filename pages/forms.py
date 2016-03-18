from django import forms
from django.contrib.flatpages.forms import FlatpageForm
from pages.models import *
from django.contrib.flatpages.models import FlatPage


class add_to_mailing_list_form(forms.Form):

    auto_id = False

    email_address = forms.EmailField(max_length=255)
    mailing_list_id = forms.HiddenInput()


class send_message_form(forms.Form):

    message_from = forms.EmailField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    message = forms.CharField(max_length=255, label='', widget=forms.Textarea(attrs={'placeholder': 'Name'}))


class FlatPageForm(FlatpageForm):

    url = forms.CharField(help_text="e.g. /how-it-works/general-info/earning-spending/", label="", widget=forms.TextInput(attrs={'placeholder': 'Page URL'}))
    title = forms.CharField(help_text="e.g. Earning &amp; Spending", label="", widget=forms.TextInput(attrs={'placeholder': 'Page Title'}))
    content = forms.CharField(help_text="Please follow the <a href='/style-guide/' target='_blank'>Ithacash Web Style Guide</a>", label="", widget=forms.Textarea(attrs={'placeholder': 'Page Content'}))

    # Default values
    enable_comments = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hide'}), required=False)
    registration_required = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hide'}), required=False)
    sites = forms.ChoiceField(widget=forms.Select(attrs={'class': 'hide'}), choices=(('1', 'ithacash.com'),), initial='1')
    template_name = forms.CharField(help_text="The template that this page will be based on (defaults to flatpages/template.html)", widget=forms.TextInput(), initial="flatpages/template.html")


class SubPageForm(forms.ModelForm):

    class Meta:
        model = SubPage
        fields = {'heading', 'meta_desc', 'meta_keywords', 'meta_image'}

    heading = forms.CharField(help_text="e.g. Earning &amp; Spending", label="", widget=forms.TextInput(attrs={'placeholder': 'Page Heading'}))
    meta_desc = forms.CharField(help_text="Succinct Ithacash description", initial="Ithacash", label="", widget=forms.Textarea(attrs={'placeholder': 'Meta Description'}))
    meta_keywords = forms.CharField(help_text="e.g. ithaca, currency, local", initial="ithaca, local, currency", label="", widget=forms.TextInput(attrs={'placeholder': 'Meta Keywords'}))
    meta_image = forms.CharField(initial="https://ithacash.com/static/img/ithacash_logo_rgb_325x124.png", label="", widget=forms.TextInput(attrs={'placeholder': 'Meta Image'}))


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = UploadedFiles
        fields = {'file'}

    file = forms.FileField(
        label='Select a file',
        help_text='Images to be shown on pages should be below 50kb. Full-size images should be available via a link only'
    )
    # title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Image Title'}))
