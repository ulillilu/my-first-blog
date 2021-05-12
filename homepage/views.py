from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #name = "Michael"
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums})