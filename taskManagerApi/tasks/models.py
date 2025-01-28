from django.db import models

# Create your models here.
class TaskManager(models.Model):
    """This class will contain the model which will handle task submissions and store them."""
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.title