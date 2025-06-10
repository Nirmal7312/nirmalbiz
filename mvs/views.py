from django.shortcuts import render


def mvs(request):
    return render(request, 'mvs/mvs.html')
