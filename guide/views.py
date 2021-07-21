from django.shortcuts import render, HttpResponse


def guidehome(request):
    return render(request, 'guide/guide-all.html')
