from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from resume.forms import createForm, RegistrationForm, resumeViewForm, resumeEditForm, resumeDeleteForm, \
    resumepublicForm
from resume.models import Create

@login_required(login_url='loginPage')
def index(request):
    return render(request,"resume/index.html")
def resumeCreate(request,pk):
    form=createForm(initial={'uid':pk,"user":request.user})
    context={}
    context['form']=form
    qs=Create.objects.all()
    context['obj']=qs
    if request.method=="POST":
        form=createForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createresume')
    return render(request,"resume/createresume.html",context)

def Register(request):
    form=RegistrationForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
        else:
            context={}
            context['form']=form
        return render(request, "resume/registration.html", context)
    return render(request,"resume/registration.html",context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        print(username,",",password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("loginPage")
    return render(request,'resume/login.html')

def logoutpage(request):
    logout(request)
    return redirect("loginPage")

def resumeview(request,pk):
    qs=Create.objects.get(id=pk)
    context={}
    context['user']=qs
    return render(request,"resume/resumeview.html",context)

def resumeEdit(request,pk):
    qs=Create.objects.get(id=pk)
    form=resumeEditForm(instance=qs)
    context={}
    context["form"]=form
    if request.method=="POST":
        qs =Create.objects.get(id=pk)
        form=resumeEditForm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createresume")
    return render(request,"resume/resumeedit.html",context)

def resumeDelete(request,pk):
    product=Create.objects.get(id=pk)
    form=resumeDeleteForm(instance=product)
    context={}
    context["form"]=form
    if request.method == "POST":
        product = Create.objects.get(id=pk)
        form =resumeDeleteForm(instance=product, data=request.POST)
        if form.is_valid():
            product.delete()

            return redirect("createresume")
    return render(request,"resume/resumedelete.html",context)

def viewresume(request):
    obj=Create.objects.filter(user=request.user)
    context={}
    context['obj']=obj
    return render(request,"resume/resumepublic.html", context)

def resumedetails(request,pk):
    qs =Create.objects.get(id=pk)
    context = {}
    context['obj'] = qs
    return render(request,"resume/publicview.html",context)

def home(request):
    return render(request,"resume/home.html")