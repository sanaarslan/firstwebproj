from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("<h1>welcome response is working</h1>")

#
# def downloads(request):
#     return HttpResponse("<h1> No Downloads </h1>")

def home(request):
    return render(request,"index.html",{"key1":"i m coming from python code"})

def result(request):
    # age=request.GET['user_age']
    # name=request.GET['user_name']
    # message=f'Hi,{name},you are {age}years old'

    article=request.GET['article']
    words=article.split()
    word_count=len(words)
    return render(request,'result.html',{'article':article,'word_count':word_count})