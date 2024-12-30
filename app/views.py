from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_country(request):
    cn=input('enter country name')
    ci=int(input('enter country id'))
    ca=input('enter country abbrev')
    CO=Country.objects.get_or_create(cou_name=cn,
                                     cou_id=ci,
                                     cou_abb=ca)
    if CO[1]:
        return HttpResponse('New country Details Are Updated')
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
        return HttpResponse('New capital details are updated')
    else:
        return HttpResponse('the given details r already present')
    
#displaying from back-end to front-end

def display_country(request):
    LCO=Country.objects.all()
    dic={'LCO':LCO}
    return render(request,'display_country.html',dic)

def display_capital(request):
    LCAO=Capital.objects.all()
    dic={'LCAO':LCAO}
    return render(request,'display_capital.html',dic)