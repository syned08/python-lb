from django.test import TestCase
from django.urls import reverse, resolve
from ..views import index, go_link


class TestUrls(TestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_index_url_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_go_link_url_is_resolved(self):
        url = reverse('go_link', args=[6])
        self.assertEquals(resolve(url).func, go_link)
