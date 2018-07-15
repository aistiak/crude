from django.shortcuts import render
from .models import store 
# Create your views here.

def IndexView(request):

    return render(request,'img/index.html')

def addImgView(request):

    imgFile = request.GET['image']
    name  = "demoImgName"
    s = store(img_file=imgFile,img_name=name)
    s.save();   
    context = {
        'store':s,
    } 
    return render(request,'img/index.html',context)


  