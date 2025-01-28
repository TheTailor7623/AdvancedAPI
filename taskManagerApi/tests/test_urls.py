from django.test import TestCase
from django.urls import reverse

class TestTaskManagerApp(TestCase):
    """This class will serve to test the task manager app"""
    def setUp(self):
        self.validHomeURL = reverse("home")

    def test_empty_url_path_leads_to_app(self):
        """This function tests that a valid empty URL path leads to the app"""
        response = self.client.get(self.validHomeURL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Task Manager!")
