from django.shortcuts import render
import MySQLdb
from myapp.models import Sangdata
from django.http.response import HttpResponseRedirect
# Create your views here.
config = {  # 기본값

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3306,

    'charset':'utf8',

    'use_unicode':True

}

def Main(request):
    
    sangdata = Sangdata.objects.all().order_by('-code') 
    

    
    return render(request,'list.html',{'sangdata':sangdata})
    
    

    


def InsertFunc(request):
    return render(request, 'insert.html')



def InsertOkFunc(request):
    if request.method == 'POST':
        #print(request.POST.get('sang'))
        Sangdata(
            code = request.POST.get('code'),
            sang = request.POST.get('sang'),
            su = request.POST.get('su'),
            dan = request.POST.get('dan')
            
            ).save()
    
    return HttpResponseRedirect('main') # 추가 후 목록보기
    #return render(request, 'insert.html')


def UpdateFunc(request):
    data = Sangdata.objects.get(sang = '장갑') # 부분데이터
    print(data)
    print(data.sang)
    
    return render(request,'update.html',{'sang_one':data})

    
def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save() # 수정완료
    
    return HttpResponseRedirect('main')
        
        
        
def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('main')

  