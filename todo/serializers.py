from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from todo.models import Todoitem,Todolist

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id', 'name', 'creation_date')
class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ('id', 'description', 'completed','due_by','todolist')