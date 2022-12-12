from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

challenges_by_months = {
    "jan": "It's Jan",
    "feb": "It's Feb",
    "mar": "It's Mar",
    "apr": "It's Apr",
    "may": "It's May",
    "jun": "It's Jun",
    "jul": "It's Jul",
    "aug": "It's Aug",
    "sept": "It's Sept",
    "oct": "It's Oct",
    "nov": "It's Nov",
    "dec": "It's Dec",
}


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    try:
        what = challenges_by_months[month]
        return HttpResponse(what)
    except:
        return HttpResponseNotFound("Kakka")
