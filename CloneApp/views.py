from django.shortcuts import render

# Create your views here.

def main(req):
    return render(req,'main.html')
def home(req):
    return render(req,'home.html')
def course(req):
    return render(req,'course.html')
def bootcamp(req):
    return render(req,'bootcamp.html')
def request(req):
    return render(req,'request.html')
def signin(req):
    return render(req,'signin.html')