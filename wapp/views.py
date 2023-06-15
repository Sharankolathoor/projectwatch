from django.shortcuts import render,redirect
from wapp.models import branddb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def homepage(r):
    return render(r,"home.html")
def brandpage(r):
    return render(r,"addbrand.html")
def savebrand(r):
    if r.method=="POST":
        bname=r.POST.get('bn')
        bimage=r.FILES['bi']
        desc=r.POST.get('des')
        obj=branddb(bname=bname,bimage=bimage,desc=desc)
        obj.save()
        messages.success(r,"New brand added")
        return redirect(brandpage)
def displaybrand(r):
    bdata=branddb.objects.all()
    return render(r,"displaybrand.html",{'bdata':bdata})
def editbrand(r,brandid):
    bdata=branddb.objects.get(id=brandid)
    return render(r,"editbrand.html",{'bdata':bdata})
def updatebrand(r,brandid):
    if r.method=="POST":
        bname=r.POST.get('bn')
        desc = r.POST.get('des')
        try:
            bimage = r.FILES['bi']
            fs=FileSystemStorage()
            brimage=fs.save(bimage.name,bimage)
        except MultiValueDictKeyError:
            brimage=branddb.objects.get(id=brandid).bimage
        branddb.objects.filter(id=brandid).update(bname=bname,bimage=brimage,desc=desc)
        return redirect(displaybrand)
def deletebrand(r,brandid):
    bdata=branddb.objects.get(id=brandid)
    bdata.delete()
    return redirect(displaybrand)
def productpage(r):
    bdata=branddb.objects.all()
    return render(r,"addproduct.html",{'bdata':bdata})
def saveproduct(r):
    if r.method=="POST":
        brand=r.POST.get('br')
        pname=r.POST.get('pn')
        desc=r.POST.get('des')
        pimage=r.FILES['pi']
        price=r.POST.get('pz')
        obj=productdb(brand=brand,pname=pname,des=desc,pimage=pimage,price=price)
        obj.save()
        messages.success(r,"New product added")
        return redirect(productpage)
def displayproduct(r):
    product=productdb.objects.all()
    return render(r,"displayproduct.html",{'product':product})
def editproduct(r,p_id):
    bdata=branddb.objects.all()
    product=productdb.objects.get(id=p_id)
    return render(r,"editproduct.html",{'product':product,'bdata':bdata})
def updateproduct(r,p_id):
    if r.method=="POST":
        brand=r.POST.get('br')
        pname=r.POST.get('pn')
        des=r.POST.get('des')
        price=r.POST.get('pz')
        try:
            pimage=r.FILES['pi']
            fs=FileSystemStorage()
            primage=fs.save(pimage.name,pimage)
        except MultiValueDictKeyError:
            primage=productdb.objects.get(id=p_id).pimage
        productdb.objects.filter(id=p_id).update(brand=brand,pname=pname,des=des,price=price,pimage=primage)
        return redirect(displayproduct)

def deleteproduct(r,p_id):
    product=productdb.objects.get(id=p_id)
    product.delete()
    return redirect(displayproduct)
def loginpage(r):
    return render(r,"loginpage.html")
def adminlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                return redirect(homepage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)






