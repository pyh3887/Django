from django.shortcuts import render
from myapp.models import Sangpum, Sangpum2
from django.http.response import HttpResponseRedirect, HttpResponse
import json

# Create your views here.


def Main(request):
    
    return render(request,'main.html')


def InsertFunc(request):
    
    return render(request,'insert.html')    
    

def Insertok(request):

    Sangpum2(
            sang_val = request.POST.get('checkbtn'),
            sang_name = request.POST.get('name'),
            sang_pay = request.POST.get('pay'),
            sang_stock = request.POST.get('stock'),
            sang_explain = request.POST.get('explain')
            ).save()
            
            
    return HttpResponseRedirect('adminpage') 
    


def AdminFunc(request):        
    
    
    
    return render(request,'admin.html')


def Showlist(request):
    
    sangpum = Sangpum2.objects.all()
    
    datas = [] 
    for s in sangpum:
    
        dicData = {"id":s.sang_id , 'val':s.sang_val, 'name':s.sang_name, 'pay': s.sang_pay, 'stock': s.sang_stock,'explain': s.sang_explain}
        datas.append(dicData) # [{'code':s.code....}...]
   
    
    return HttpResponse(json.dumps(datas) , content_type= 'application/json')



def BugerFunc(request):
    
    bugerdata = Sangpum2.objects.all().filter(sang_val = 1)
    
    
    datas = [] 
    for s in bugerdata:
    
        dicData = {"id":s.sang_id , 'val':s.sang_val, 'name':s.sang_name, 'pay': s.sang_pay, 'stock': s.sang_stock,'explain': s.sang_explain}
        datas.append(dicData) # [{'code':s.code....}...]
   
    
    return HttpResponse(json.dumps(datas) , content_type= 'application/json')
    

def DrinkFunc(request):
    
    drinkdata = Sangpum2.objects.all().filter(sang_val = 2)
    
    
    datas = [] 
    for s in drinkdata:
    
        dicData = {"id":s.sang_id , 'val':s.sang_val, 'name':s.sang_name, 'pay': s.sang_pay, 'stock': s.sang_stock,'explain': s.sang_explain}
        datas.append(dicData) # [{'code':s.code....}...]
   
    
    return HttpResponse(json.dumps(datas) , content_type= 'application/json')



def SubmitFunc(request):
    msg = request.GET['su']
    msg1 = request.GET['gap']
    
    
    
    data = Sangpum2.objects.all().filter(sang_id = msg)
    
    aa = int(data[0].sang_pay) * int(msg1)
    dicData = {"hap":aa}
       
    return HttpResponse(json.dumps(dicData) , content_type= 'application/json')
    
    
    
    
    
    

    