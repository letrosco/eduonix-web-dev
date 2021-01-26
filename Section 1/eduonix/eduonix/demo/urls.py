from django.urls import path

from . import views # from current directory add the views.py file

urlpatterns = [
    path('', views.index, name='index'), # define the index view as the root
    path('<str:name>', views.hello, name='hello'), # non blank goes to the hello page
]