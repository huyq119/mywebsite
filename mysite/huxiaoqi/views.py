from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("你好,世界,我在这里等你很久了")

