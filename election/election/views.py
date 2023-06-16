from django.shortcuts import render
from .models import Agent,Lgaresult,Unitresult,Lga,Polling_Unit,State,Ward


def showagent(request):
    agents = Agent.objects.all()

    context = {
        'Agent' : agents
    }
    return render(request, "agent.html", context)


def showlgaresults(request):
    lgaresults = Lgaresult.objects.all()

    context = {
        'lgaresult' : lgaresults
    }
    return render(request, "lgaresult.html", context)

def showunitresults(request):
    unitresults = Unitresult.objects.all()

    context = {
        'unitresult' : unitresults
    }
    return render(request, "unitresult.html", context)


def state(request):
    state = State.objects.all()

    context = {
        'state' : state
    }
    return render(request, "state.html", context)


def lga(request):
    lga = Lga.objects.all()

    context = {
        'lga' : lga
    }
    return render(request, "lga.html", context)

def ward(request):
    ward = Ward.objects.all()

    context = {
        'ward' : ward
    }
    return render(request, "ward.html", context)



def pollingunit(request):
    p_unit = Polling_Unit.objects.all()

    context = {
        'p_unit' : p_unit
    }
    return render(request, "polling_unit.html", context)

def newunit(request):
    return render(request, "new_unit.html")