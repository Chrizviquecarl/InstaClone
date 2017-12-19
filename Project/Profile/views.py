from django.http import HttpResponse

def profile(Request):
    return HttpResponse("<h1>Profile Page</h1>")