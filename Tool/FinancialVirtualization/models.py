from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    risk_type = models.CharField(max_length=10)

# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.username