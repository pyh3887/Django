from django.shortcuts import render
import MySQLdb
from company.models import Gogek, Jikwon
from collections import ChainMap
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



def ListFunc(request):
    
    return render(request,'list.html')


def GogekFunc(request):
    
   
    
    name = request.POST.get('name')
    tel = request.POST.get('tel')
    flag = request.POST.get('flag')
          
    data = Gogek.objects.filter(gogek_name=name,gogek_tel=tel).values_list('gogek_damsano')
    print(data)
    print(data)
    
    queryset = Gogek.objects.all().select_related('gogek_damsano')
    
   # aa = queryset[0]..jikwon_name
    
    #print("나야나" , aa)
    
    try:
        sql = '''select jikwon_name,jikwon_jik,buser_name,buser_tel,
            CASE 
            when jikwon_gen = '남' then 'man.png'
            when jikwon_gen = '여' then 'women.png' END AS jikwon_gen
            ,TIMESTAMPDIFF(YEAR, jikwon_ibsail,NOW()) as jikwon_ibsail,
            CASE 
            when jikwon_rating = 'a' then '최우수'
            when jikwon_rating = 'b' then '우수'
            when jikwon_rating = 'c' then '일반'
            END AS jikwon_rating          
         from jikwon join gogek on gogek_damsano = jikwon_no join buser on buser_num = buser_no 
         where gogek_name = "{0}" and gogek_tel = "{1}" '''.format(name,tel)
         
        conn = MySQLdb.connect(**config)
        # print(conn)
        cursor = conn.cursor()
        cursor.execute(sql) 
        datas = cursor.fetchall()
        
        
        if datas != None:
            
            flag = 'y'
       
          
            
    except Exception as e :
        print('idcheckFunc err :' + str(e))
        
    print(flag)
    return render(request,'list.html',{'data':datas,'flag':flag})




