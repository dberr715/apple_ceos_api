from django.db import models


# Create your models here.
class AppleCeo(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=256)
    year_started = models.IntegerField(null=True)

    def __str__(self):
        return self.name
