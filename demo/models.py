from django.db import models


# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=30)
    minsal = models.IntegerField(null=True)
    maxsal = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} - {self.minsal} to {self.maxsal}"
