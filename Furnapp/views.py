import datetime

from django.shortcuts import render,redirect
from Furnapp.models import CategoryDb
from Furnapp.models import ProductDb
from WebApp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages



# Create your views here.
def indexpage(request):

    return render(request,"indexpage.html")
def AddCategory(req):
    return render(req,"AddCategory.html")

def Save_Category(request):
    if request.method == "POST":
        a = request.POST.get('Category')
        b = request.POST.get('Description')
        c = request.FILES['image']
        obj = CategoryDb(Category=a,Description=b,Category_Image=c)
        obj.save()
        messages.success(request, "Category Saved...")
        return redirect(AddCategory)
def display_Categories(req):
    data = CategoryDb.objects.all()
    return render(req,"DisplayCat.html",
                  {'data':data})

def EditCategories(req,cat_id):
    dat = CategoryDb.objects.get(id=cat_id)
    return render(req,"EditCat.html",
    {'dat':dat})
def Update_Category(request,cat_id):
    if request.method == "POST":
        cat = request.POST.get('Category')
        desc = request.POST.get('Description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cat_id).Category_Image
        CategoryDb.objects.filter(id=cat_id).update(Category=cat,Description=desc,Category_Image=file)
        return redirect(display_Categories)

def Addproduct(req):
    cat = CategoryDb.objects.all()
    return render(req,"Addproduct.html",{'cat':cat})
def Save_Product(request):
    if request.method == "POST":
        a = request.POST.get('Category')
        b = request.POST.get('Product')
        c = request.POST.get('Quantity')
        d = request.POST.get('MRP')
        e = request.POST.get('Description')
        f = request.POST.get('Country')
        g = request.POST.get('Manufactured')
        h = request.FILES['image1']
        i = request.FILES['image2']
        j = request.FILES['image3']
        obj = ProductDb(Product_Category=a,Product_Name=b,Quantity=c,MRP=d,Description=e,Country=f,Manufactured=g,Image1=h,Image2=i,Image3=j)
        obj.save()
        messages.success(request, "Product Saved...!")
        return redirect(Addproduct)
def display_Product(req):
    datas = ProductDb.objects.all()
    return render(req,"Displayproduct.html",
                  {'datas':datas})
def EditProduct(req,dat_id):
    dataa = ProductDb.objects.get(id=dat_id)
    return render(req,"EditPro.html",
    {'dataa':dataa})
def Update_Product(request,P_id):
    if request.method == "POST":
        ab = request.POST.get('Category')
        bb = request.POST.get('Product')
        cb = request.POST.get('Quantity')
        db = request.POST.get('MRP')
        eb = request.POST.get('Description')
        fb = request.POST.get('Country')
        gb = request.POST.get('Manufactured')
        try:
            img = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=P_id).Image1
        try:
            imgs = request.FILES['image2']
            fci = FileSystemStorage()
            file2 = fci.save(imgs.name, imgs)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=P_id).Image2
        try:
            imggs = request.FILES['image3']
            ffc = FileSystemStorage()
            file3 = ffc.save(imggs.name, imggs)
        except MultiValueDictKeyError:
            file3 = ProductDb.objects.get(id=P_id).Image3
        ProductDb.objects.filter(id=P_id).update(Product_Category=ab,Product_Name=bb,Quantity=cb,MRP=db,Description=eb,Country=fb,Manufactured=gb,Image1=file1,Image2=file2,Image3=file3)
        return redirect(display_Product)
def DeleteProduct(request,Pro_id):
    x= ProductDb.objects.filter(id=Pro_id)
    x.delete()
    messages.error(request, "Data deleted...!")
    return redirect(display_Product)
def DeleteCat(request,C_id):
    y= CategoryDb.objects.filter(id=C_id)
    y.delete()
    messages.error(request,"Data deleted...!")
    return redirect(display_Categories)
def login_page(req):
    return render(req, "adminloginpage.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request,"Welcome..!")
                return redirect(indexpage)
            else:
                messages.error(request,"Please Check your password..!")
                return redirect(login_page)
        else:
            messages.warning(request,"Invalid Username...!")
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Successfully logout")
    return redirect(login_page)
def display_Contact(req):
    data = ContactDb.objects.all()
    return render(req,"Displaycontact.html",
                  {'data':data})
def DeleteContact(req,Con_id):
    x = ContactDb.objects.filter(id=Con_id)
    x.delete()
    return redirect(display_Contact)




