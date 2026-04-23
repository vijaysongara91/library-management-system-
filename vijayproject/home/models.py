from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject = models.TextField(null=True, blank=True) 
    message=models.TextField()

    def __str__(self)-> str:
        return self.name



