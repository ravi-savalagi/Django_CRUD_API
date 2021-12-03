from django.db import models

# Create your models here.
class  Employee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField(('email'), null=True, blank=True)
    mobile = models.CharField(max_length=12,blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(('address'), max_length=150, null=True, blank=True)

    def __str___(self):
        return self.first_name
