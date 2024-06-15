# models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    doctor = models.CharField(max_length=100)  # Add this field

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"