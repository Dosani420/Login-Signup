from django.shortcuts import render,redirect,HttpResponse
from .models import person

# Create your views here.

def index(request):

    return render(request,'index.html')

def signup(request):

    return render(request,'Signup.html')

def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        person1 = person(
            name=fullname,
            email=email,
            password=password,
            role=role
        )
        person1.save()

        return redirect('index')

    return render(request, "Signup.html")

def login(request):
    if request.method == "POST":
        em = request.POST.get("email")
        password = request.POST.get("password")
        person1 = person.objects.all()
        for p in person1:
            if p.email ==  em and p.password == password:
                d= {"name":p.name}
                return render(request, "home.html",d)
        else:
            return HttpResponse("Wrong username or password")
    else:
        return render(request, "index.html")

