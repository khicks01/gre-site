from django.db import models

# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField("date added", auto_now_add=True)
    def __str__(self):
        return self.email
    