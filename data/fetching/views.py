from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    name = "Victor"
    age = 25
    return render(request, "fetching/index.html", {'name': name, 'age':age})
def about(request):
    return render(request, "fetching/about.html")
def contact (request):
    return render(request, "fetching/contact.html")
def blog(request):
    return render(request, "fetching/blog.html")