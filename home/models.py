from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    # phone = models.PhoneNumberField(blank=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    name = models.EmailField()

    def __str__(self):
        return self.name
    
class Request(models.Model):
    name = models.CharField(max_length=250)
    request = models.TextField()

    def __str__(self):
        return self.name

