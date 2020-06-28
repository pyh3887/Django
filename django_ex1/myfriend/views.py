from django.shortcuts import render
from myfriend.models import Article

# Create your views here.




def Main(request):
    return render(request,'main.html')


def Dbtest(request):
    datas = Article.objects.all() 
    print(datas[0],datas[1],datas[2])
    return render(request,'articlelist.html',{'articles':datas})