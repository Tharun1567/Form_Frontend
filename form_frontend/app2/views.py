from django.shortcuts import render

# Create your views here.
def func2(request):
    result=None
    
    if request.method=="POST":
        a=int(request.POST.get('num'))
        if a%2==0:
            result=True
        else:
            result=False
    return render(request,'evenodd.html',{'res':result})

def func3(request):
    result=None
    
    if request.method=="POST":
        a=int(request.POST.get('num'))
        if a%2!=0 and a%a==0 and a%1==0:
            result=True
        else:
            result=False
    return render(request,'prime.html',{'res':result})

def func4(request):
    a=None
    b=None
    result=None
    print(request.GET)
    print(request.POST)
    if request.method == "POST":
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        if a>b:
            result = True
        else:
            result = False
    return render(request, "greatest.html", context={"res": result, "n1": a, "n2": b})

def func5(request):
    result=None
    
    if request.method=="POST":
        a=int(request.POST.get('num'))
        s=str(a)
        k=len(s)
        sum=0
        for num in s:
            sum+=int(num)**k
        if sum==a:
            result=True
        else:
            result=False
    return render(request,'armstrong.html',{'res':result})

def func6(request):
    d={"students":[
        {'id': 2143201, 'Name': 'THARUN K R', 'total_sub': 6,'pass_sub': 4,'fail_sub': 2},
        {'id': 2143202, 'Name': 'VINAY P', 'total_sub': 6,'pass_sub': 5,'fail_sub': 1},
        {'id': 2143203, 'Name': 'RANGA R', 'total_sub': 6,'pass_sub': 6,'fail_sub': 0},
        {'id': 2143204, 'Name': 'SAHIL S', 'total_sub': 6,'pass_sub': 6,'fail_sub': 0},
    ]}
    result = None
    if request.method=="POST":
        num=int(request.POST.get("num1"))
        print(num)
        for student in d["students"]:
            if student["id"] == num:
                result = student
                break
    context = {"result": result}
    return render(request, "studentresult.html", context)