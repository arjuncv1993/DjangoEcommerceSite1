from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import userdetails

# Create your views here.

def login(request):
    page = loader.get_template('login.html')
    try:
        path = request.POST['path']
        # print(path)
        data = {'path':path}
        response = page.render(data, request)
        return HttpResponse(response)
    except:
        
        data = {}
        response = page.render(data, request)
        return HttpResponse(response)


def register(request):
    page = loader.get_template('register.html')
    data = {}
    response = page.render(data,request)
    return HttpResponse(response)

def registeruser(request):
    if request.method == 'POST':
        username = request  .POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        # phone = request.POST['phoneno']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exists')
                return redirect('register')
            else:
                users = User.objects.create_user(username= username, first_name=firstname, last_name=lastname, email=email, password=password1)
                users.save()
                messages.info(request, 'User created Sucessfully')
                return redirect('login')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('register')
    else:
        return render(request, 'register.html')

def loguser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            path = request.POST['path']
            # print(path)
            user = auth.authenticate(username= username, password= password)
            if user is not None:
                auth.login(request, user)
                return redirect(path)
            else:
                messages.info(request, 'User does not exists.')
                return redirect('login')
        except:
            user = auth.authenticate(username= username, password= password)
            if user is not None:
                auth.login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'User does not exists.')
                return redirect('login')
    else:
        return redirect('login')
    
    
def logout(request):
    auth.logout(request)
    return redirect('homepage')

def shippingaddress(request):
    if request.method == 'POST':
        # userdb = User.objects.get(username=request.user.username)
        # username = userdb.id
        # username = userdb.username
        # print(username_id)
        # print(username)
        path = request.POST['path2']
        Address_line1 = request.POST['addressline1']
        Address_line2 = request.POST['addressline2']
        City = request.POST['city']
        State = request.POST['state']
        Phone_no = request.POST['phoneno']
        Pincode = request.POST['pincode']
        landmark = request.POST['landmark']
        user = userdetails.objects.create(Address_line1= Address_line1, Address_line2= Address_line2, City= City, 
                                          State= State, Phone_no= Phone_no, Pincode= Pincode, landmark= landmark, username_id=request.user.id)
        user.save()
        return redirect(path)
    else:
        return redirect('shippingpage')
    
def deleteaddress(request,pid):
    userdetails.objects.get(id=pid).delete()
    path = request.GET['path']
    return redirect(path)


def deleteuser(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('homepage')