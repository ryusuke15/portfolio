from __future__ import unicode_literals
from django.db import models
class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField()
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)
    def __unicode__(self):
        return self.first_name +" "+ self.last_name
