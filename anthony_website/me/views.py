from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"me/homepage.html")

def documents(request):
    return render(request, "me/documents.html")

def about(request):
    return render(request, "me/about.html")