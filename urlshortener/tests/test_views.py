from django.test import TestCase
from urlshortener.models import ShortUrl

class ViewsTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('urlshortener/home.html')

    def test_url_form_works(self):
        response = self.client.post('/', {'original_url' : "http://google.com"})
        self.assertEqual(response.status_code, 302)
        urls_count = ShortUrl.objects.all().count()
        self.assertEqual(urls_count, 1)
        url = ShortUrl.objects.get(pk = 1)
        self.assertTrue(url.generated_url)

    def test_success_page(self):
        response = self.client.post('/', {'original_url':'http://bing.com', 'suggested_suffix' : 'bing', })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/urls/1/')
        response = self.client.get('/urls/1/')
        self.assertEqual(response.status_code, 200)
        expected_url = "bing/"
        self.assertTrue(response.context['url'].generated_url, expected_url)





