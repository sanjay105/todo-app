from django.conf.urls import url
from . import views
app_name='todo'
urlpatterns=[
    url(r'^tlists/$',views.TodoListView.as_view(),name='lists'),
    url(r'^tlist/(?P<pk>[0-9]+)/$',views.TodoView.as_view(),name='item'),
    url(r'^tlist/create/$',views.TodoListCreateView.as_view()),
    url(r'^tlist/update/(?P<pk>[0-9]+)/$',views.TodoListUpdateView.as_view()),
    url(r'^tlist/delete/(?P<pk>[0-9]+)/$',views.TodoListDeleteView.as_view()),
    url(r'^titems/$',views.TodoItemView.as_view()),
    url(r'^titem/create/$',views.TodoItemCreateView.as_view()),
    url(r'^titem/update/(?P<pk>[0-9]+)/$',views.TodoItemUpdateView.as_view()),
    url(r'^titem/delete/(?P<pk>[0-9]+)/$',views.TodoItemDeleteView.as_view()),


    url(r'^r_todolists/$',views.todo_lists),
    url(r'^r_todolistdetail/(?P<pk>[0-9]+)/$',views.todo_listdetail),

    url(r'r_todolistdetail/(?P<pk>[0-9]+)/items/$',views.cid_todolist_detail),

    url(r'^r_todoitems/$',views.todo_items),
    url(r'^r_todoitemdetail/(?P<pk>[0-9]+)/$',views.todo_itemdetail),

]