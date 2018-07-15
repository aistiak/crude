from django.urls import path
from list import views 

app_name = 'list'

urlpatterns = [

    path('',views.IndexView,name='index'),
    path('detail/<str:name>',views.DetailView,name='detail'),
    path('add.html',views.AddPersonView,name='AddPerson'),
    path('AddPersonToDB',views.AddPersonToDB,name='AddPersonToDB'),
    path('editPerson/<str:name>',views.editPersonView,name='editPerson'),
    path('saveEditedPerson',views.saveEditedPerson,name='saveEdited'),

]