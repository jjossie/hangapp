from contextlib import nullcontext
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Session, User, Decision, Option

# Create your views here.

def index(request):
    return HttpResponse("Hello this is the home page yes thanks")


def start_session(request):
    # This is where a user will begin by creating questions and inviting people
    
    pass

def vote(request, decision_id):
    # This will be shown to each user to go through all the options to a decision
    decision = get_object_or_404(Decision, decision_id)
    return render(request, 'hangapp/vote.html', {'decision': decision})

