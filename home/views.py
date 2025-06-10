from django.shortcuts import render, HttpResponse


#home
def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')



