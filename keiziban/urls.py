from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:article_id>', views.edit, name = 'edit'),
    path('delete/<int:article_id>', views.delete, name = 'delete'),
]