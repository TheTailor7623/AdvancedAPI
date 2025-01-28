from django.test import TestCase
from tasks import models
from datetime import date

class TestTaskManagerApp(TestCase):
    """This class will serve to test the models in this project"""
    def setUp(self):
        """This function will contain data used throughout testing"""
        # Valid data
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a description for the test task.',
            'due_date': date.today(),
            'status': 'todo'
        }

        self.task_data_high_boundary_title = {
            'title': 'Test Task Test Task Test Task Test Task Test Task Test Task Test Task Test Task Test Task Test Task',
            'description': 'This is a description for the test task.',
            'due_date': date.today(),
            'status': 'todo'
        }

        self.task_data_high_boundary_description = {
            'title': 'Test Task',
            'description': 'This is a description for the test task This is a description for the test task This is a description for the test task This is a description for the test task This is a description for the test task',
            'due_date': date.today(),
            'status': 'todo'
        }

        self.task_data_high_boundary_years = {
            'title': 'Test Task',
            'description': 'This is a description for the test task.',
            'due_date': date(date.today().year + 100, 1, 1),
            'status': 'todo'
        }

        # Invalid data
        self.invalid_title_length = "Invalid title" * 100

    # Test valid title inputs
    def test_valid_title(self):
        """This tests that the task model can handle valid TITLE inputs"""
        result = models.TaskManager.objects.create(
            title = self.task_data["title"],
            description = self.task_data["description"],
            due_date = self.task_data["due_date"],
            status = self.task_data["status"],
        )
        self.assertEqual(result.title, self.task_data["title"])

    def test_high_boundary_title(self):
        """This tests that the task model can handle high boundary valid TITLE inputs"""
        result = models.TaskManager.objects.create(
            title = self.task_data_high_boundary_title["title"],
            description = self.task_data_high_boundary_title["description"],
            due_date = self.task_data_high_boundary_title["due_date"],
            status = self.task_data_high_boundary_title["status"],
        )
        self.assertEqual(result.title, self.task_data_high_boundary_title["title"])

    # Test invalid title inputs
    def test_invalid_title_inputs(self):
        """This tests that the task model can handle invalid TITLE inputs"""
        with models.TaskManager.objects.create(
            title = self.invalid_title_length,
            description = self.task_data["description"],
            due_date = self.task_data["due_date"],
            status = self.task_data["status"],
        ):
            self.assertRaises(ValueError)

    # Test valid description inputs
    def test_valid_description(self):
        """This tests that the task model can handle valid DESCRIPTION inputs"""
        result = models.TaskManager.objects.create(**self.task_data)
        self.assertEqual(result.description, self.task_data["description"])

    def test_high_boundary_description(self):
        """This tests that the task model can handle valid DESCRIPTION inputs"""
        result = models.TaskManager.objects.create(
            title = self.task_data_high_boundary_description["title"],
            description = self.task_data_high_boundary_description["description"],
            due_date = self.task_data_high_boundary_description["due_date"],
            status = self.task_data_high_boundary_description["status"],
        )
        self.assertEqual(result.description, self.task_data_high_boundary_description["description"])

    # Test valid date inputs
    def test_valid_date_input(self):
        """This tests that the task model can handle valid DUE_DATE inputs"""
        result = models.TaskManager.objects.create(**self.task_data)
        self.assertEqual(result.due_date, self.task_data["due_date"])

    def test_high_boundary_date_input(self):
        """This tests that the task model can handle valid DUE DATE inputs"""
        result = models.TaskManager.objects.create(
            title = self.task_data_high_boundary_years["title"],
            description = self.task_data_high_boundary_years["description"],
            due_date = self.task_data_high_boundary_years["due_date"],
            status = self.task_data_high_boundary_years["status"],
        )
        self.assertEqual(result.due_date, self.task_data_high_boundary_years["due_date"])

    # Test valid status inputs
    def test_valid_status_input(self):
        """This tests that the task model can handle valid STATUS inputs"""
        result = models.TaskManager.objects.create(**self.task_data)
        self.assertEqual(result.status, self.task_data["status"])

    def test_task_model_is_available(self):
        """This tests that the model is available"""
        pass
