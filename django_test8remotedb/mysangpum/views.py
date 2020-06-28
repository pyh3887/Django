from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def MainFunc(request):
    
    return render(request,'main.html')



def ListFunc(request):
    '''
    conn = '' 
    sql = 'select * from sangdata'
    cursor = conn.cursor()
    cursor.excute(sql)
    datas = cursor.fetchall()  return type이 tuple 이므로 {{키.0}} 
    '''
    
    # --페이지 나누기 기능은 list2.html 로 출력
    datas = Sangdata.objects.all().order_by('-code') #ORM return type 이 QuerySet
    paginator = Paginator(datas,5)   
    
    #페이징설정
    
    try:
        page = request.GET.get('page')
    
    except:
        page =1
        
    try:
        data = paginator.page(page)
    
    except PageNotAnInteger:
        data = paginator.page(1)
    
    except EmptyPage:
        data =paginator.page(paginator.num_pages())
        
    # 개별 페이지 표시용 작업
    
    allpage = range(paginator.num_pages + 1)
    print('allpage:', allpage)   
     
    
     
    return render(request,'list2.html',{'sangpums': data,'allpage':allpage},)
 
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
    
    return HttpResponseRedirect('/sangpum/list') # 추가 후 목록보기
    

def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code')) # 부분데이터
    
    
    
    return render(request,'update.html',{'sang_one':data})
    
def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save() # 수정완료
    
    return HttpResponseRedirect('/sangpum/list')
        
def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list')
