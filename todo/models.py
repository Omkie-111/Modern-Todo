from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    title = models.CharField(max_length=100)  # Title of the todo item
    description = models.CharField(max_length=1000)  # Description of the todo item
    due_date = models.DateField(blank=True, null=True)  # Due date of the todo item
    tags = models.JSONField(blank=True, null=True)  # Tags associated with the todo item
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')  # Status of the todo item

    def __str__(self):
        return self.title  # Return the title as the string representation of the todo item
    
    def save(self, *args, **kwargs):
        if self.pk:  # Check if it's an existing entry
            raise ValueError("Cannot edit the timestamp field.")  # Prevent editing the timestamp field
        super().save(*args, **kwargs)  # Call the save method of the superclass

