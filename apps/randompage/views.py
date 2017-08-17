from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if ('counter' not in request.session):
        request.session['counter'] = 0
    unique_id = get_random_string(length=14)
    randword = {
        'word' : unique_id
    }
    return render(request,'randomepage/index.html', randword)

def generator(request): 
    request.session['counter'] += 1
    unique_id = get_random_string(length=14)
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    print request.session
    return redirect('/')

    
        