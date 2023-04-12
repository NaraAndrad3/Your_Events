from django.shortcuts import render
from django .http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def new_event(request):
    if request.method == "GET":
        return render(request,'new_event.html')
    elif request.method == "POST":
        pass
