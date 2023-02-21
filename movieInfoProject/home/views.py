from django.shortcuts import render

def homeView(request):
    intro = 'Hello World!'
    return render(request, 'home.html', locals())