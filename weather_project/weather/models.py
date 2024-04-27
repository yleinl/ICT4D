from django.db import models

class Weather(models.Model):
    date = models.DateField()
    forecast = models.CharField(max_length=200)

    def __str__(self):
        return str(self.date)
