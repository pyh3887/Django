from django.shortcuts import render
from setapp.models import Gogek
from django.http.response import HttpResponse
import json

# Create your views here.


def mainFunc(request):
    
    
    return render(request,'main.html')
    
    




def DataList(request):
    
    jikdata = Gogek.objects.all().select_related('gogek_damsano')
    
  
    datas = [] 
    for s in jikdata:
        print(s.gogek_damsano.jikwon_name)
        dicData = {"gogek_name":s.gogek_name ,                   
                    'jikwon_no': s.gogek_damsano.jikwon_no, 
                    'jikwon_name': s.gogek_damsano.jikwon_name}
        
        datas.append(dicData) # [{'code':s.code....}...]   
    
    print(datas)
    return HttpResponse(json.dumps(datas) , content_type= 'application/json')





