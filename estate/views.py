from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Service,About,Team,Comment
from .forms import Detailsform,Commentform
from django.contrib.auth import logout
def index(request):
    data=Service.objects.all()
    comment=Comment.objects.all()
    form=Commentform()
    if request.method=='POST':
        form=Commentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=Commentform()
            return redirect("/")
    context={
        "data":data,
        "comment":comment,
        "form":form
    }
    return render (request,"index.html",context)
def about(request):
    data=About.objects.all()
    team=Team.objects.all()
    context={
        "data":data,
        "team":team
    }
    return render (request,"about.html",context)
@login_required
def service(request):
    form=Detailsform()
    if request.method=='POST':
        form=Detailsform(request.POST)
        if form.is_valid():
            form.save()
            form=Detailsform()
            return redirect("/")
    return render(request,"service.html",{"form":form})
def more(request):
    more(request)
    return redirect("about")
def registration(request):
    form=UserCreationForm() 
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=UserCreationForm() 
            return redirect("/")
        return redirect("/") 
    return render(request,"registration.html",{"form":form}) 
def logout(request):
    logout(request)
    return redirect("/")


