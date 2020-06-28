from django.shortcuts import render
from myapp.models import Article

# Create your views here.


def Main(request):
    return render(request,'main.html')


def Dbtest(request):
    datas = Article.objects.all() # Django의 ORM select * from Article (myapll_article)
    #print(datas[0].sang)
    
    return render(request,'articlelist.html',{'articles':datas})