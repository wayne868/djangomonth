from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes!",
    "march": "Learn Django for 20 minutes a day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes!",
    "june": "Learn Django for 20 minutes a day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes!",
    "september": "Learn Django for 20 minutes a day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes!",
    "december": "Learn Django for 20 minutes a day!",
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li>...</li><li>...</li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month - 1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize(),
        })
    except:
        return HttpResponseNotFound("<h1>This is not a valid month!</h1>")
