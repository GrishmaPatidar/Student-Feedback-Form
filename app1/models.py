
from django.db import models

class Feedback(models.Model):
    COURSE_CHOICES = [
        ('fsd', 'Full Stack development'),
        ('dsa', 'Data structures and Algorithms'),
        ('ai', 'Artificial Intelligence'),
        ('java', 'Advanced Java'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    rating = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.name





