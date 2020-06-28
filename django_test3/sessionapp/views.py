from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def main(request):
    return render(request,'main.html')

def setos(request):
    
    if "favorite_os" in request.GET:
        #print(request.GET['favorite_os'])
        request.session['f_os'] = request.GET['favorite_os'] # 세션 생성
        return HttpResponseRedirect('/showos')  # showos요청이 발생
    
    else:
        return render(request,'setos.html')
        

def showos(request):
    context = {} #dict key value
    
    if 'f_os' in request.session: #세션 키중에서 f_os 가 있다면
        context['f_os'] = request.session['f_os']   #f_os 키에다 담아주기  request.session.get('f_os')
        context['message'] = '선택한 운영체제는 %s'%request.session['f_os']
    
    else : 
        context['f_os'] = None
        context['message'] = 'ㅠㅠ 운영체제를 선택하지 못했네요'
    
    request.session.set_expiry(5) # 세션 시간 5초간 유효
    return render(request,'show.html', context)
    