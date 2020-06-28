from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def MainFunc(request):
    return render(request,'index.html')

class Callview(TemplateView):
    template_name = 'callget.html'
    

def InsertFunc(request):
    return render(request,'insert.html')


def InsertokFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')  
        irum = request.GET.get('name')
        
        return render(request, 'list.html',{'irum':irum})
    
    
    if request.method == 'POST':
        print('POST 요청 처리')       
        irum = request.POST.get('name')
        
        return render(request, 'list.html',{'irum':irum})
        
     
    else: 
        print('요청 오류')
        



