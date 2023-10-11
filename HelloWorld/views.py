from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")  # Replace this with your desired content for the index page
