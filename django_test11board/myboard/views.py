from django.shortcuts import render
from myboard.models import BoardTab
from django.core.paginator import Paginator,PageNotAnInteger , EmptyPage
from django.http.response import HttpResponseRedirect
from datetime import datetime



# Create your views here.


def Main(request):
    
    aa = "<div><h1>메인화면</h1></div>"
    return render(request,'main.html',{'main': aa})




def ListFunc(request):
    
    #datas = BoardTab.objects.all().order_by('-id')
    
    datas = BoardTab.objects.all().order_by('-gnum','onum')
    
    paginator = Paginator(datas,5) # 한페이지당 5 행 출력
    
    page = request.GET.get('page')
    
    try:
        data = paginator.page(page)
        
    
    except PageNotAnInteger:
        
        data = paginator.page(1)
    
    except EmptyPage:
        
        data = paginator.page(paginator.num_pages())
        
    
    return render(request, 'board.html' , {'data': data})




def InsertFunc(request):
    
    return render(request, 'insert.html')
   



def InsertokFunc(request):
    if request.method == 'POST':
        try:
            
            gbun = 1
            datas= BoardTab.objects.all() # group 번호 구하기
            if datas.count() != 0 :
                print('dd')
                gbun = BoardTab.objects.latest('id').id + 1
                print(datetime.now())
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],
                readcnt = 0,
                bdate = datetime.now(),                
                gnum = gbun,
                onum = 0,
                nested = 0,                                                
                ).save()            
        except: 
            print('insertokfunc err')
            
            
            
    return HttpResponseRedirect('/board/list')


def SearchFunc(request): #검색용
    
    if request.method == 'POST' :
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        
        if s_type == 'title' : 
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id') # 칼럼명 __ contains는 like 연산자 처럼 작업됌
            
        elif s_type == 'name' :
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
            
        paginator = Paginator(datas,5) # 한페이지당 5 행 출력
    
        page = request.GET.get('page')

            
    try:
        data = paginator.page(page)
        
    
    except PageNotAnInteger:
        
        data = paginator.page(1)
    
    except EmptyPage:
        
        data = paginator.page(paginator.num_pages())
        
    
    return render(request, 'board.html' , {'data': data})
    
    

def ContentFunc(request): # 상세보기
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt = data.readcnt + 1
    data.save() # 조회수 1 증가
    page = request.GET.get('page')
    return render(request,'content.html',{'data_one':data, 'page':page})    
    
    
def UpdateFunc(request):
    
    try:
        data = BoardTab.objects.get(id= request.GET.get('id'))
    
    except Exception as e:
        print('UpdateFunc err : ' + str(e))
        
        
        
    return render(request,'update.html', {'data_one':data})        
    

def UpdateOkFunc(request):
    
    if request.method == 'POST':
        upRec = BoardTab.objects.get(id = request.POST.get('id'))
        #비밀번호 비교 
        if upRec.passwd == request.POST.get('up_passwd'):
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont')            
            upRec.save()
        else:
            return render(request,'error.html')       
        
    return HttpResponseRedirect('/board/list') # 수정후 목록보기



def DeleteFunc(request):
    
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except:
        print('deletefunc err')
    
    return render(request,'deleteok.html',{'data':data})
        
        

def DeleteOkFunc(request):
    deldata = BoardTab.objects.get(id = request.POST.get('id'))
    if(deldata.passwd == request.POST.get('del_passwd')) :
        deldata.delete()
        return HttpResponseRedirect('/board/list')
        
        

def ReplyFunc(request):
    try:
        redata = BoardTab.objects.get(id=request.GET.get('id'))
    
    except Exception as e:
        print('reply err' , e)
    
    return render(request, 'reply.html', {'data_one':redata})

    
def ReplyOkFunc(request):
    if request.method == 'POST' :
        try:
            
            regnum = int(request.POST.get('gnum'))
            reonum = int(request.POST.get('onum'))
            
            tempRec = BoardTab.objects.get(id = request.POST.get('id'))
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_gnum >= reonum and old_gnum == regnum:
                old_onum = old_onum + 1 #onum 갱신
                
            # 댓글 저장 
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],
                readcnt = 0,
                bdate = datetime.now(),                
                gnum = regnum,
                onum = old_onum,
                nested = int(request.POST.get('nested')) + 1,                            
                ).save()
                
                
            
        except Exception as e:
            print('ReplyOkFunc err:' + str(e))
    
        
    return HttpResponseRedirect('/board/list') # 수정후 목록보기
    