from django.shortcuts import render

# Create your views here.
def func1(request):
    a=request.POST.get('sname')
    print(a)
    return render(request,'index.html',{'res':a})
