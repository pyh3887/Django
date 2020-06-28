from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime
# Create your views here.

def MainFunc(request):
    return render(request,'main.html')


def ListFunc(request):
    gdata = Guest.objects.all() #ORM. id별 ascending sort 가 기본
    #gdata = Guest.objects.all().order_by('id') # 정렬방법 1 order_by
    #gdata = Guest.objects.all().order_by('title') 
    #gdata = Guest.objects.all().order_by('-title') # descending sort
    #gdata = Guest.objects.all().order_by('-id')[0:2] #       
    return render(request, 'list.html' , {'gdata':gdata})  # forward




def InsertFunc(request):
    return render(request,'insert.html')


def insertOkFunc(request):
    if request.method == 'POST':
        #print(request.POST.get('title'))
        #print(request.Post['title'])
        
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()
            
            ).save() # ORM 추가
        
        return HttpResponseRedirect('/guest') # 추가 후 목록보기
    
    else : 
        return HttpResponseRedirect('/guest/insert')
        
