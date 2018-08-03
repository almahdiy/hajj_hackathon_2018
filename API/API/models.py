from django.db import models
from datetime import datetime
from django.utils import timezone
from django import forms

class TrafficLight(models.Model):
    #ID is a default field.
    lng = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    #status = models.IntegerField(default=0)
    persons = models.IntegerField(default=0)
    area = models.FloatField(default=0)


    # def __str__(self):
    #     return "Username: " + self.username