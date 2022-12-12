from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):

    the_list = list(challenges_by_months)

    loops_months = ""
    for month in the_list:
        capmonth = month.capitalize()
        pathmonth = reverse("month-challenges", args=[month])
        loops_months += f"<li><a href=\"{pathmonth}\">{capmonth}</a></li>"

    response = f"<ul>{loops_months}</ul>"

    return HttpResponse(response)


def monthly_challenges_by_number(request, month):
    forwarded_month = list(challenges_by_months.keys())

    if month > len(forwarded_month) or month == 0:
        return HttpResponseNotFound("Kakka")

    thenumberpath = forwarded_month[month-1]
    reversedpath = reverse("month-challenges", args=[thenumberpath])
    return HttpResponseRedirect(reversedpath)


def monthly_challenges(request, month):
    try:
        what = challenges_by_months[month]
        return render(request, "challenges/challenge.html", {"text": what, "month": month})
    except:
        return HttpResponseNotFound("Kakka")
