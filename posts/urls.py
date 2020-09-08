from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list,name = 'posts'),
    path('create/',views.create_post,name = 'create'),
    path('details/',views.post_details,name= 'details'),
    path('update/',views.post_update,name ='update'),
    path('delete/',views.post_delete,name = 'delete'),
]
