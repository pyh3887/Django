from django.shortcuts import render
from company.models import Buser, Jikwon, Gogek

# Create your views here.
import MySQLdb

# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')

# print(conn)

# conn.close

config = {  # 기본값

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3306,

    'charset':'utf8',

    'use_unicode':True

}


def BuserFunc(request):
    data = Buser.objects.all()    
    return render(request, 'buser.html', {'buser':data})


def JikwonFunc(request):    
    
    data = Jikwon.objects.all().filter(buser_num=request.GET.get('buser_no'))
    
    return render(request, 'jikwon.html', {'jikwon':data})
    pass


def GogekFunc(request):
    no = str(request.GET.get('jikwon_no'))

    
    try:
        conn = MySQLdb.connect(**config)
        # print(conn)
        cursor = conn.cursor()  # SQL 문 수행을 위한 커서 객체 생성
        sql = 'select  gogek_no,gogek_name,CASE when SUBSTR(gogek_jumin, 8, 1) = "1" then "남" ELSE "여" END as gogek_gen,gogek_tel from gogek where gogek_damsano = "{0}"'.format(no)
        cursor.execute(sql) 
        data = cursor.fetchall()        
        print(data[0])
      
    except Exception as e :
        print('err:' , e)

    finally:
        conn.close()
  
    return render(request, 'gogek.html', {'gogek':data})
 
