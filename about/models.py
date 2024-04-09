from django.db import models

# Create your models here.

class About(models.Model):
    """
    Stores a single about me text
    """
    
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Feedback(models.Model):
    """
    Stores a single feedback message
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback from {self.name}"
