from django import forms
from django.contrib.flatpages.forms import FlatpageForm


class newsletter_subscription_form(forms.Form):

    auto_id = False

    subscriber_email_address = forms.EmailField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))


class send_message_form(forms.Form):

    message_from = forms.EmailField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    message = forms.CharField(max_length=255, label='', widget=forms.Textarea(attrs={'placeholder': 'Name'}))


class PageCreatorForm(FlatpageForm):

    def __init__(self, *args, **kwargs):
        super(PageCreatorForm, self).__init__(*args, **kwargs)

    url = forms.CharField(help_text="e.g. /how-it-works/general-info/earning-spending/", label="", widget=forms.TextInput(attrs={'placeholder': 'Page URL'}))
    title = forms.CharField(help_text="e.g. Earning &amp; Spending", label="", widget=forms.TextInput(attrs={'placeholder': 'Page Title'}))
    content = forms.CharField(help_text="Please follow the <a href='/style-guide/' target='_blank'>Ithacash Web Style Guide</a>", label="", widget=forms.Textarea(attrs={'placeholder': 'Page Content'}))

    # Default values
    enable_comments = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hide'}), initial=False, required=False)
    registration_required = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hide'}), initial=False, required=False)
    sites = forms.ChoiceField(widget=forms.Select(attrs={'class': 'hide'}), choices=(('1', 'ithacash.com'),), initial='1')
    template_name = forms.CharField(help_text="The template that this page will be based on (defaults to flatpages/template.html)", widget=forms.TextInput(), initial="flatpages/template.html")
