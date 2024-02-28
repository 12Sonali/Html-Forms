from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        username=request.POST['un']
        return  HttpResponse('username')
    return render(request,'htmlforms.html')

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Schoolname']   
            sp=SFDO.cleaned_data['Schoolprincipal']
            sl=SFDO.cleaned_data['Schoollocation']
            e=SFDO.cleaned_data['email']
            r=SFDO.cleaned_data['reenteremail']
            SO=School.objects.get_or_create(Schoolname=sn,Schoolprincipal=sp,Schoollocation=sl,email=e,reenteremail=r)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_school.html',d)
