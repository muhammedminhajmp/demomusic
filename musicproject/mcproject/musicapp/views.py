from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import music
from . forms import MusicForm
# Create your views here.
def index(request):
    mc=music.objects.all()
    context={
        'music_list':mc
    }

    return render(request,'index.html',context)
def detail(request,music_id):
    music1=music.objects.get(id=music_id)
    return render(request,"detail.html",{'music':music1})

def add_music(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        music1=music(name=name,desc=desc,year=year,img=img)
        music1.save()

    return render(request,'add.html')

def update(request,id):
    music2=music.objects.get(id=id)
    form=MusicForm(request.POST or None,request.FILES,instance=music2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'music':music2})

def delete(request,id):
    if request.method=='POST':
        music3=music.objects.get(id=id)
        music3.delete()
        return redirect('/')
    return render(request,'delete.html')
