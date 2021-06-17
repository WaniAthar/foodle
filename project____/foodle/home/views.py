from django.shortcuts import render, HttpResponse

# Create your views here.
def about(requests):
    return HttpResponse("This is about page")
def index(requests):
    context = {
        'variable' : "POST TEST OVER"
    }
    return render(requests, 'index.html', context)
    # return HttpResponse("This is homepage")
def services(requests):
    return HttpResponse("This is dummy page lklklk")