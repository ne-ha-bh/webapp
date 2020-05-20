from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.welcome),
    path('form/', views.load_form),
    path('add/', views.add),
    path('showall/', views.show_all),
    path('edit<int:id>/', views.edit),
    path('update<int:id>/', views.update),
    path('delete<int:id>/', views.delete),
    path('search/', views.search),
]
