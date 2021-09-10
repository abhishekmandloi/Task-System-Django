from django.urls import path
from . import views
app_name = 'taskapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('createTask', views.createTask, name = 'createTask'),
    path('editTask/<int:pk>', views.editTask, name = 'editTask'),
    path('viewTask/<int:pk>', views.viewTask, name = 'viewTask'),
]
