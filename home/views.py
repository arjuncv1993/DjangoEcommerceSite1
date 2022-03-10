from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import itemlist, cartitems
import random
from django.contrib.auth.models import User, auth
from account.models import userdetails
from django.contrib import messages



# Create your views here.

def homepage(request):
    page = loader.get_template('homepage.html')
    # print(random.choice(range(10)))
    # db = itemlist.objects.all()
    # print(random.choices(population))
    datalist = []
    listofno = []
    while True:
        if len(listofno) == 20:
            break
        else:
            # print(i)
            # print(len(itemlist.objects.all()))
            num = random.choice(range(1,len(itemlist.objects.all())))
            if num not in listofno:
                listofno.append(num)
    # print(listofno)
    for i in listofno:
        # print(i)
        db = itemlist.objects.get(Item_No = i)
        # print(db.Item_Name)
        datalist.append({'name': db.Item_Name,
                         'price': db.Price,
                         'id':db.Item_No,
                         })
    # print(datalist)
    username = request.user.username
    data = {'pros': datalist, 'idname': username}
    # print(data)
    response = page.render(data, request)
    return HttpResponse(response)


def itempage(request,pid):
    page = loader.get_template('item_page.html')
    db = itemlist.objects.get(Item_No= pid)
    # print(db.Features)
    features = {'specs' : db.Features.split(',')}
    # print(features)
    data = {'pros':db, 'spec': features, 'tdb': itemlist.objects.all()}
    response = page.render(data, request)
    return HttpResponse(response)

def productpage(request, category):
    page = loader.get_template('products.html')
    db = itemlist.objects.filter(Category__contains = category)
    data = {'pros': db, 'cat': category}
    response = page.render(data, request)
    return HttpResponse(response)

def addtocart(request):
    if request.method == 'POST':
        proid = request.POST['itemno']
        qty = request.POST['qty']
        userid = request.user.id
        # db = itemlist.objects.get(Item_No=proid)
        print(userid)
        try:
            db = cartitems.objects.get(Product_id=proid)
            # print(db)
            cartitems.objects.get(Product_id=proid).delete()
            # print('item deleted')
            user = cartitems.objects.create(Qty=qty, Product_id=proid, username_id=userid)
            user.save()
            # print('new data saved')
        except:
            # print('no data')
            user = cartitems.objects.create(Qty=qty, Product_id=proid, username_id=userid)
            user.save()
            # print('data saved')
        return redirect('mycart')
            
    else:
        return HttpResponse()

def cartpage(request):
    page = loader.get_template('cart.html')
    cartdb = cartitems.objects.filter(username_id=request.user.id)
    # print(cartdb.Product_id)
    cartlist = []
    total = 0
    for i in cartdb:
        itemdb = itemlist.objects.get(Item_No=i.Product_id)
        # print(itemdb.Brand)
        cartlist.append({'name':itemdb.Item_Name, 'price':itemdb.Price, 'qty':i.Qty, 'total_price':itemdb.Price*i.Qty,'id':i.Product_id})
    # print(cartlist)
    for i in cartlist:
        for k,v in i.items():
            if k == "total_price":
                total += v
    nos = len(cartlist)
    data = {'pros': cartlist, 'total': total, 'Nos':nos}
    response = page.render(data, request)
    return HttpResponse(response)


def deletecartitem(request,pid):
    cartitems.objects.get(Product_id=pid).delete()
    return redirect('mycart')


def shippingpage(request):
    page = loader.get_template('shippingpage.html')
    # shippingaddress = userdetails.objects.filter(username.username=request.user.username)
    # data = {"add": shippingaddress}
    db = userdetails.objects.filter(username_id=request.user.id)
    print(db)
    # print(db.username.first_name)
    data = {"add": db}
    response = page.render(data, request)
    return HttpResponse(response)


def placeorder(request):
    if request.method == 'POST':
        page = loader.get_template('placeorder.html')
        try:
            address_selection_id = request.POST['id']
            # print(address_selection_id)
            addressdb = userdetails.objects.get(id=address_selection_id)
            cartdb = cartitems.objects.filter(username_id=request.user.id)
            cartlist = []
            total = 0
            for i in cartdb:
                itemdb = itemlist.objects.get(Item_No=i.Product_id)
                cartlist.append({'name':itemdb.Item_Name, 'qty':i.Qty, 'price':itemdb.Price*i.Qty})
            for i in cartlist:
                for k,v in i.items():
                    if k == "price":
                        total += v
            data = {'add': addressdb, 'items': cartlist, 'total':total}
            response = page.render(data, request)
            return HttpResponse(response)
        except:
            messages.info(request, "Please select a valid address")
            return redirect('shippingpage')
    else:
        return HttpResponse("Request method error")
            

def searchitem(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        # print(keyword)
        itemdata = itemlist.objects.filter(Item_Name__contains = keyword) | itemlist.objects.filter(Category__contains = keyword) | itemlist.objects.filter(Features__contains= keyword)
        print(itemdata)
        data = {'keyword': keyword, 'pros': itemdata}
        page = loader.get_template('searchitem.html')
        response = page.render(data, request)
        return HttpResponse(response)
    else:
        return HttpResponse("Request method Error")


def userprofile(request):
    page = loader.get_template('profilepage.html')
    db = userdetails.objects.filter(username_id=request.user.id)
    print(db)
    data = {"add": db}
    response = page.render(data, request)
    return HttpResponse(response)