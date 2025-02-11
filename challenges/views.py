from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This is not a valid month!")
    return HttpResponse(challenge_text)
