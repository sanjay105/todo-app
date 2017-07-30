# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework.parsers import JSONParser

from todo.models import Todolist, Todoitem
from todo.serializers import TodolistSerializer, TodoitemSerializer


class TodoListView(ListView):
    model=Todolist
    context_object_name ='tlists'

class TodoListCreateView(CreateView):
    model=Todolist
    fields = ['name','creation_date']

class TodoView(DetailView):
    model=Todolist
    context_object_name = 'todoli'
    template_name = "todo/litem_list_id.html"

    def get_context_data(self, **kwargs):
        context = super(TodoView, self).get_context_data(**kwargs)
        context['itlists'] = Todoitem.objects.all().filter(todolist=self.object)
        return context

class TodoListUpdateView(UpdateView):
    model=Todolist
    fields = ['name', 'creation_date']

class TodoListDeleteView(DeleteView):
    model=Todolist
    success_url = reverse_lazy('todo:todolist')

class TodoItemView(ListView):
    model=Todoitem
    context_object_name ='tlists'

class TodoItemCreateView(CreateView):
    model=Todoitem
    fields = ['description','completed','due_by','todolist']

class TodoItemUpdateView(UpdateView):
    model=Todoitem
    fields = ['description','completed','due_by','todolist']

class TodoItemDeleteView(DeleteView):
    model=Todoitem
    success_url = reverse_lazy('todo:todoitem')



@csrf_exempt
def cid_todolist_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stud = Todoitem.objects.filter(todolist_id=pk)
        print stud
    except Todoitem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoitemSerializer(stud, many=True)
        return JsonResponse(serializer.data, safe=False)

        # serializer = TodoitemSerializer(stud)
        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoitemSerializer(stud, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stud.delete()
        return HttpResponse(status=204)
@csrf_exempt
def todo_lists(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets =Todolist.objects.all()
        serializer = TodolistSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodolistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def todo_listdetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        college = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodolistSerializer(college)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodolistSerializer(college, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        college.delete()
        return HttpResponse(status=204)


@csrf_exempt
def todo_items(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets =Todoitem.objects.all()
        serializer = TodoitemSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoitemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def todo_itemdetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        college = Todoitem.objects.get(pk=pk)
    except Todoitem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoitemSerializer(college)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoitemSerializer(college, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        college.delete()
        return HttpResponse(status=204)