from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, I am starting my fist django project and a new error occured")