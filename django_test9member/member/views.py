from django.shortcuts import render
from member.models import MemTable
import MySQLdb
from django.http.response import HttpResponseRedirect

# Create your views here.

config = {  # 기본값

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'dbmember',

    'port':3306,

    'charset':'utf8',

    'use_unicode':True

}

def Main(request):
    
    return render(request,'main.html')



def ListFunc(request):
    datas = MemTable.objects.all()
    
    return render(request,'list.html',{'members':datas})
    

def IdcheckFunc(request):
    memid = request.GET.get('memid')
        
    isRegister = False #해당 id 등록 여부 판단
    
    try:
        # 방법1 장고 ORM 사용
        #data = MemTable.objects.get(memid = memid)
        #print('data :' ,data) # 없으면 exception err 를 만남
        #isRegister = True
        
        
        # 방법2
        sql = 'select * from member_memtable where memid = "{}"'.format(memid)
        conn = MySQLdb.connect(**config)
        # print(conn)
        cursor = conn.cursor()
        cursor.execute(sql) 
        data = cursor.fetchone()
        #print 
        if data != None:
            isRegister = True
        
        
                  
        
             
    except Exception as e :
        print('idcheckFunc err :' + str(e))
    
    
    return render(request,'idcheck.html',{'memid':isRegister,'id':memid})
    
     



def ZipcheckFunc(request):
    chk = request.GET.get('check')
    
    return render(request,'zipcheck.html',{'check':chk})
                


def ZipcheckOkFunc(request):
    area3 = request.POST.get('area3')
    
    conn = MySQLdb.connect(**config)
    sql = 'select * from member_ziptab where area3 like "{}%"'.format(area3)
        # print(conn)
    cursor = conn.cursor()
    cursor.execute(sql) 
    datas = cursor.fetchall()
    
    print(datas)
    cursor.close()
    conn.close()
    return render(request, 'zipcheck.html',{'datas':datas,'check':'n'})    
    




def InsertFunc(request):
    
    if request.method == 'GET':
        return render(request,'insert.html')
    
    elif request.method == 'POST':
        MemTable(
             memid = request.POST.get('memid'),
             passwd = request.POST.get('passwd'),
             name = request.POST.get('name'),
             email = request.POST.get('email'),
             phone = request.POST.get('phone'),
             zipcode = request.POST.get('zipcode'),
             address = request.POST.get('address'),
             job = request.POST.get('job'),
            ).save()
            
        
        return HttpResponseRedirect('/member/list') #등록후 목록보기
    
    else:
        return render(request,'error.html')