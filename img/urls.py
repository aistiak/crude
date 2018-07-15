from django.urls import path
from img import views 

app_name = 'img'

urlpatterns = [

    path('',views.IndexView,name='Imgindex'),
    path('addImg',views.addImgView,name='AddImg'),
    

]