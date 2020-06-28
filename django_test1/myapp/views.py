from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('인덱스 요청 처리')



def helloFunc(request):
    msg = '장고'
    imsi = '<html><body>장고 수행 메세지 :%s </body></html>'%(msg,)
    return HttpResponse(imsi)

def hello_tem(request):
    mymsg = '홍길동'
    return render(request,'show.html',{'msg':mymsg})


def worldFunc(request):
    
    return render(request,'disp.html')