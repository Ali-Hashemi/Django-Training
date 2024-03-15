from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days = {
    'saturday': 'this is saturday',
    'sunday': 'this is sunday',
    'monday': 'this is monday',
    'tuesday': 'this is tuesday',
    'wednesday': 'this is wednesday',
    'thursday': 'this is thursday',
    'friday': 'this is friday',
}


def days_list(request):
    days_list = list(days.keys())
    list_items = ""
    for day in days_list:
        url_path = reverse('days-of-week', args=[day])
        list_items += f'<li><a href="{url_path}">{day}</a></li>'

    content = f'<ul> \n {list_items}\n</ul>'

    return HttpResponse(content)


def dynamic_days_by_numbder(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')

    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])  # /days/sunday
    return HttpResponseRedirect(redirect_url)


def dynamic_days(request, day):
    day_data = days.get(day)
    if day_data is not None:
        response_data = f'<h1>day is : {day} and data is :{day_data}</h1>'
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound('day does not exists')
