from django.db import models
import jsonfield


class Schema(models.Model):
    name = models.CharField(max_length=64)
    schema = jsonfield.JSONField(blank=True)
