"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
>>>>>>> 7d5f087c4e99aa85f4ff913899c3075425769d76
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from app.views import home, form, create, view, edit, update,delete
=======
from app.views import delete, home, form, create, view, edit, update, delete
>>>>>>> 7d5f087c4e99aa85f4ff913899c3075425769d76

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
<<<<<<< HEAD
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
=======
    path('view/<int:pk>/',view, name='view'),
    path('edit/<int:pk>/',edit, name='edit'),
    path('update/<int:pk>/',update, name='update'),
>>>>>>> 7d5f087c4e99aa85f4ff913899c3075425769d76
    path('delete/<int:pk>/', delete, name='delete'),
]
