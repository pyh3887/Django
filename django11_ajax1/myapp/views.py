from django.shortcuts import render
import json
from django.http.response import HttpResponse


# Create your views here.

lan = {
    'id': 111, 
    'name': '파이썬',
    'history':[
        {'date' :'2020-5-20','exam':'basic'},
        {'date' :'2020-5-21','exam':'django'},
        ]
    }



def good(request):
    print(type(lan))
    # JSON encoding
    
    jsonString = json.dumps(lan) # json 형태로 변환
    
    print(jsonString,'',type(jsonString))    
    
    jsonString = json.dumps(lan,indent =4)
    print(jsonString)
    
    print()
    
    # JSON decoding -- str ==> python object ------
    dict = json.loads(jsonString)    
    print(dict)
    print(type(dict))
    print(dict['name'])
    
    for h in dict['history']:
        print(h['date'], ' ' , h['exam'])
    


def Main(request):
    
    #good()
     
    
    
    return render(request,'main.html')


def ajax(request):
    msg = request.GET['msg']
    print(msg, type(msg))
    context = {'key': msg}
    print(context, type(context))
    print(json.dumps(context), ' ' ,type(json.dumps(context)))
    return HttpResponse(json.dumps(context), content_type = 'application/json')
    
    
    
    
     
     
    
    
    return render(request,'main.html')