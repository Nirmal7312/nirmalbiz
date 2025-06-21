from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    number = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name