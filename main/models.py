from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
