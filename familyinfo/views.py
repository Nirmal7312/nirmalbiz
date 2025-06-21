from django.shortcuts import render, HttpResponse, redirect
from .models import Family

def index(request):
    family = Family.objects.all()
    return render(request, 'familyinfo/index.html', {'family':family})


def delete(request, did):
    data = Family.objects.filter(id=did)
    data.delete()
    return redirect('index')


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        age = request.POST.get('age')
        family = Family(name=name, number=number, age=age)
        family.save()
        return redirect('index')
    return render(request, 'familyinfo/add.html')
