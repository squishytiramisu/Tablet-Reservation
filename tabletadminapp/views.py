from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Nap,Foglalas,Kornyezeti
from datetime import date,timedelta
from django import forms
from django.contrib.auth import authenticate,login
# Create your views here.


#TODO: A torles ne legyen egy szar, tudja a napot meg a oraszamot vagy hozza kene adni egy idt fuk

def hetnapja(nap):
    hetnapjai=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek","Szombat","Vasárnap"]
    return hetnapjai[date(nap.ev,nap.ho,nap.nap).weekday()]


def cserelegyet_fifo():
    #oldest?
    oldest=Nap.objects.last()
    ujdate=date(oldest.ev,oldest.ho,oldest.nap)+timedelta(days=1)
    Nap.objects.first().delete()
    Nap.objects.create(ev=ujdate.year,ho=ujdate.month,nap=ujdate.day)

class UjForm(forms.Form):
    nev=forms.CharField(label='Tanár neve:')
    ora=forms.IntegerField(label='Hanyadik óra: ',min_value=1,max_value=6)
    db=forms.IntegerField(label='Darab',min_value=1,max_value=20)

def index(request):
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("bejelentkezes"))
    
    
    #ameddig nem a mai nap a legrégebbi
    if request.method == "POST":
        keres=request.POST
        keres = dict(keres)
        print(keres)
        id=keres["id"][0]
        Foglalas.objects.filter(id=id).delete()



    
    while  not ((Nap.objects.first().nap == date.today().day) and (Nap.objects.first().ho == date.today().month)):
        cserelegyet_fifo()

    
    
    
    adatok=[]
    
    for nap in Nap.objects.all():
        #napnev=hetnapjai[date(nap.ev,nap.ho,nap.nap).weekday()]
        napnev=hetnapja(nap)
        azorak=[]
        for oraszam in range(1,Kornyezeti.objects.filter(alap=1)[0].napioraszam+1):
            azorak.append({"osszesen":0,"posts":[]})
        for foglalas in Foglalas.objects.all():
            if foglalas.nap.nap==nap.nap:
                azorak[foglalas.oraszam-1]["osszesen"]+=foglalas.mennyiseg
                azorak[foglalas.oraszam-1]["posts"].append({"tanar":foglalas.tanar,"db":foglalas.mennyiseg,"id":foglalas.id})
        adatok.append({"napnev":napnev,"orak":azorak,"napszam":nap.nap})
        #adatok.append({"napnev":napnev,"orak":[{"osszesen":7,"posts":[{"tanar":"Mária","db":5},{"tanar":"Lajos","db":2}]},{"osszesen":10,"posts":[{"tanar":"Fox","db":5},{"tanar":"Alfred","db":2}]}]})

    return render(request,"tabletapp/index.html",{"god":adatok,"elerheto":Kornyezeti.objects.filter(alap=1)[0].elerhetotablet})

def hozzadas(request,napszam):
    for egyesnap in Nap.objects.all():
        if egyesnap.nap==napszam:
            xd=egyesnap
    if request.method == "POST":
        form =UjForm(request.POST)
        if form.is_valid():
            nev=form.cleaned_data["nev"]
            db=form.cleaned_data["db"]
            orasorszam=form.cleaned_data["ora"]
            Foglalas.objects.create(tanar=nev,mennyiseg=db,oraszam=orasorszam,nap=xd)
            return HttpResponseRedirect(reverse("index"))

        else:
           return render(request,"tabletapp/hozzadas.html",{"form":form,"napszam":napszam})
    else:
        print("debug")
        return render(request,"tabletapp/hozzadas.html",{"form":UjForm(),"napszam":napszam,"napneve":hetnapja(xd)})



def bejelentkezes(request):
    if request.method == "POST":
        username="tanar"
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"tabletapp/bejelentkezes.html",{"message":"Sajnos ez nem a megfelelő kód!"})


    return render(request,"tabletapp/bejelentkezes.html")
