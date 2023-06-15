from django.shortcuts import render,redirect
from wapp.models import branddb,productdb
from webapp.models import registerdb,contactdb,cartdb,checkoutdb
from django.contrib import messages

# Create your views here.
def hompage(r):
    bdata=branddb.objects.all()
    return render(r,"hom.html",{'bdata':bdata})
def productpage(r,brand_name):
    bdata=branddb.objects.all()
    prdata=productdb.objects.filter(brand=brand_name)
    return render(r,"productpage.html",{'prdata':prdata,'bdata':bdata})
def aboutpage(r):
    return render(r,"aboutpage.html")
def contactpage(r):
    return render(r,"contactpage.html")
def savecontact(r):
    if r.method=="POST":
        name=r.POST.get('name')
        email=r.POST.get('email')
        subject=r.POST.get('sub')
        message=r.POST.get('msg')
        obj=contactdb(name=name,email=email,subject=subject,message=message)
        obj.save()
        return redirect(contactpage)
def singleproduct(r,prid):
    bdata=branddb.objects.all()
    prsingle=productdb.objects.get(id=prid)
    return render(r,"singleproductpage.html",{"prsingle":prsingle,'bdata':bdata})
def registerpage(r):
    return render(r,"registrationpage.html")
def saveregister(r):
    if r.method=="POST":
        uname=r.POST.get('un')
        email=r.POST.get('em')
        mobile=r.POST.get('mob')
        password=r.POST.get('pw')
        profile=r.FILES['pro']
        obj=registerdb(username=uname,email=email,mobile=mobile,password=password,profile=profile)
        obj.save()
        messages.success(r,"Registration completed")
        return redirect(registerpage)
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        if registerdb.objects.filter(username=uname,password=password).exists():
            request.session['username']=uname
            request.session['password']=password
            messages.success(request,"Log In successfully")
            return redirect(hompage)
        else:
            messages.error(request,"Invalid username or password")
            return redirect(registerpage)
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(hompage)
def cartpage(r):
    bdata=branddb.objects.all()
    cdata=cartdb.objects.filter(c_username=r.session['username'])
    # cartdata=cartdb.objects.all()
    return render(r,"cartpage.html",{'cdata':cdata,'bdata':bdata})
def savecart(r):
    if r.method=="POST":
        uname=r.POST.get('username')
        pname=r.POST.get('name')
        description=r.POST.get('des')
        quantity=r.POST.get('qty')
        price=r.POST.get('price')
        tprice=r.POST.get('tot')
        # image=r.FILES['pimage']
        obj=cartdb(c_username=uname,c_pname=pname,c_description=description,c_quantity=quantity,c_price=price,c_totalprice= tprice)
        obj.save()
        messages.success(r,"Item added to cart")
        return redirect(cartpage)
def deletecart(r,cartid):
    cartdata=cartdb.objects.filter(id=cartid)
    cartdata.delete()
    messages.success(r,"Successfully removed")
    return redirect(cartpage)
def checkoutpage(r):
    cdata=cartdb.objects.filter(c_username=r.session['username'])
    return render(r,"checkout.html",{'cdata':cdata})
def savecheckout(r):
    if r.method=="POST":
        fname=r.POST.get('fname')
        lname=r.POST.get('lname')
        phone=r.POST.get('phone')
        email=r.POST.get('email')
        country=r.POST.get('country')
        address=r.POST.get('address')
        town=r.POST.get('town')
        district=r.POST.get('district')
        pin=r.POST.get('pin')
        obj=checkoutdb(ck_fname=fname,ck_lname=lname,ck_phone=phone,ck_email=email,ck_country=country,ck_address=address,ck_town=town,ck_district=district,ck_pin=pin)
        obj.save()
        messages.success(r,"Order placed")
        return redirect(hompage)


