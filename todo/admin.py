# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import Todolist,Todoitem
# Register your models here.
admin.site.register(Todolist)
admin.site.register(Todoitem)