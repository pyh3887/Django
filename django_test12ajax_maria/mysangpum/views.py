from django.shortcuts import render
from mysangpum.models import Sangdata

import json
from django.http.response import HttpResponse

# Create your views here.


def Main(request):
    
    return render(request, 'main.html')



def List(request):
    
    return render(request,'list.html')  
    
    


def CallDb(request):
    
    sangdata = Sangdata.objects.all()    
    datas = [] 
    
    for s in sangdata:
    
        dicData = {'code':s.code, 'sang':s.sang, 'su': s.su, 'dan': s.dan}
        datas.append(dicData) # [{'code':s.code....}...]
    print(datas)
    
    
    return HttpResponse(json.dumps(datas) , content_type= 'application/json')