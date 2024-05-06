from django.shortcuts import render

def history(requests):
    return render(requests, 'history.html')