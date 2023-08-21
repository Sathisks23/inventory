from django.shortcuts import render ,redirect
from .models import Product, Location, ProductMovement
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render(request,"index.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def reg(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        

        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Already taken")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('reg')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect ('/')
        else:
            messages.info(request,"password does not match")
            return redirect('reg')
    else:
        
        return render(request,'reg.html')
    

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,'Inavild credentials')
            return redirect('log')
    else:
        return render(request,'login.html')

# Define other views for locations and product movements as needed
