from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the poll index")
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." %poll_id)
def results(request, poll_id):
    return HttpResponse("You're looking at the results from poll %s" % poll_id)
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" %poll_id)