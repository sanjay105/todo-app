# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length=128)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Todoitem(models.Model):
    description=models.CharField(max_length=512)
    completed=models.BooleanField(default=False)
    due_by=models.DateField()
    todolist=models.ForeignKey(Todolist)
    def __unicode__(self):
        return self.description
