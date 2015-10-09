from django.test import TestCase
from pages.models import SubPage
from django.contrib.flatpages.models import FlatPage
import json


class PageCreator(TestCase):

    def create_flatpage(self):

        fake_post = {'url': '/test/', 'title': 'Test Title', 'content': '<p>test</p>', 'template_name': 'fake_template.html', 'sites': '1', 'meta_desc': 'Test desc', 'meta_keywords': 'Test, keywords', 'heading': 'Test Heading'}

        self.client.post('/page-creator/', fake_post)

    def test_flatpage_creation(self):

        self.create_flatpage()

        self.assertTrue(FlatPage.objects.filter(url='/test/').exists())

    def test_flatpage_edit(self):

        self.create_flatpage()

        fake_post = {'id': '1', 'url': '/test/', 'title': 'New Test Title', 'content': '<p>test</p>', 'template_name': 'fake_template.html', 'sites': '1', 'meta_desc': 'Test desc', 'meta_keywords': 'Test, keywords', 'heading': 'Test Heading'}

        self.client.post('/page-creator/', fake_post)

        flatpage = FlatPage.objects.get(id=1)
        self.assertEqual('New Test Title', flatpage.title)

    def test_return_flatpage(self):

        self.create_flatpage()

        fake_post = {'id': '1', 'action': 'edit'}
        response = self.client.post('/page-creator/', fake_post)
        json_response = json.loads(response.content)

        self.assertEqual('Test Title', json_response['flatpage']['title'])
