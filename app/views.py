from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length

def insert_country(request):
    cn=input('enter country name')
    ci=int(input('enter country id'))
    ca=input('enter country abbrev')
    CO=Country.objects.get_or_create(cou_name=cn,
                                     cou_id=ci,
                                     cou_abb=ca)
    if CO[1]:
        #return HttpResponse('New country Details Are Updated')
        LCO=Country.objects.all()
        dic={'LCO':LCO}
        return render(request,'display_country.html',dic)
    else:
        return HttpResponse('The given details are already present')
    
def insert_capital(request):
    cn=input('enter country')
    can=input('enter capital name')
    caa=input('enter capital abbrev')
    CNO=Country.objects.get(cou_name=cn)
    CAO=Capital.objects.get_or_create(cou_name=CNO,
                                      cap_name=can,
                                      cap_abb=caa)
    if CAO[1]:
        #return HttpResponse('New capital details are updated')
        LCAO=Capital.objects.all()
        dic={'LCAO':LCAO}
        return render(request,'display_capital.html',dic)
    else:
        return HttpResponse('the given details r already present')
    
#displaying from back-end to front-end and field lookups

def display_country(request):
    LCO=Country.objects.all()
    LCO=Country.objects.all()[0:4:1]
    LCO=Country.objects.all().order_by('cou_name')
    LCO=Country.objects.all().order_by('-cou_name')
    LCO=Country.objects.exclude(cou_name='India')
    LCO=Country.objects.all().order_by('-cou_id')
    dic={'LCO':LCO}
    return render(request,'display_country.html',dic)

def display_capital(request):
    LCAO=Capital.objects.all()
    LCAO=Capital.objects.all()[0:0:-1]
    LCAO=Capital.objects.all()[0:5:1]
    LCAO=Capital.objects.all().order_by(Length('cou_name'))
    LCAO=Capital.objects.all().order_by(Length('cap_name').desc())
    dic={'LCAO':LCAO}
    return render(request,'display_capital.html',dic)

#join country and capital tables
def coucap(request):
    LCCO=Capital.objects.all().select_related('cou_name')
    LCCO=Capital.objects.select_related('cou_name').filter(cap_name__startswith='d')
    dic={'LCCO':LCCO}
    return render(request,'coucap.html',dic)