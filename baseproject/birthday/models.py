from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    name = models.CharField(max_length=40)
    address = models.TextField()
    dob  = models.DateField()
    date_of_joining = models.DateField()
    email = models.EmailField()
    phone_no = PhoneNumberField()
    
    
    def __str__(self):
        return self.name
    

    