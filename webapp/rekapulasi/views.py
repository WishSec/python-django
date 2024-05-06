from django.shortcuts import render

def rekapulasi(requests):
    return render(requests, 'rekapulasi.html')