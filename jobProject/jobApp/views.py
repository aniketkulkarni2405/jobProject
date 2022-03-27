from django.shortcuts import render,redirect
from jobApp.models import Hydjobs,Chennaijobs,Mumbaijobs,Punejobs
from .forms import createForm

def index(request):
    return render(request,"jobApp/index.html")

def HydJobsInfo(request):
    hyd_data=Hydjobs.objects.all()
    my_dict={"hyd_data":hyd_data}
    return render(request,"jobApp/hydjobs.html",my_dict)

def ChennaiJobsInfo(request):
    chennai_data=Chennaijobs.objects.all()
    my_dict={"chennai_data":chennai_data}
    return render(request,"jobApp/chennaijobs.html",my_dict)

def PuneJobsInfo(request):
    pune_data=Punejobs.objects.all()
    my_dict={"pune_data":pune_data}
    return render(request,"jobApp/punejobs.html",my_dict)

def MumbaiJobsInfo(request):
    mumbai_data=Mumbaijobs.objects.all()
    my_dict={"mumbai_data":mumbai_data}
    return render(request,"jobApp/mumbaijobs.html",my_dict)

def add_view(request):
    form=createForm()
    if(request.method=="POST"):
        form=createForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/jobApp/Chennai')
    return render(request,"jobApp/create.html",{"form":form})

def delete_view(request,id):
    opening=Chennaijobs.objects.get(id=id)
    opening.delete()
    return redirect('/jobApp/Chennai')

def update_view(request,id):
    opening=Chennaijobs.objects.get(id=id)
    if (request.method=="POST"):
        form=createForm(request.POST,instance=opening)
        if form.is_valid():
            form.save()
        return redirect('/jobApp/Chennai')
    return render(request,"jobApp/update.html",{'opening':opening})
