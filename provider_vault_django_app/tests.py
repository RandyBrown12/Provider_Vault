from django.test import TestCase, Client


class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Home", response.content
        )  # Adjust 'Home' to match actual content

    def test_main_page_status_code(self):
        client = Client()
        response = client.get("/main_page/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"ProviderVault - Medical Provider", response.content
        )  # Adjust 'Main Page' to match actual content
