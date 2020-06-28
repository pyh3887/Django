from django.shortcuts import render
from myapp.models import Profile

# Create your views here.

def index(request):
    return render(request,'index.html')


def calldict(request):
    profile_data = Profile.objects.all()
    #print(profile_data)
    pro_list = []
    
    for pro in profile_data:
        pro_dict = {}
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
        
        print(pro_list)
        
    context = {'dictdata':pro_list}
    return render(request,'list.html',context)


