# weather/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# weather_data = {
#     "Today": "Sunny, 24°C",
#     "One": "Partly cloudy, 22°C",
#     "Two": "Rainy, 18°C",
#     "Three": "Thunderstorms, 19°C",
#     "Four": "Sunny, 25°C",
#     "Five": "Cloudy, 21°C",
#     "Six": "Rain showers, 20°C",
#     "Seven": "Sunny, 23°C",
#     "Week": "Mixed weather with chances of rain midweek."
# }
#
# @csrf_exempt
# def get_weather(request):
#     if request.method == 'GET':
#         date = request.GET.get('date', 'Today')
#         return JsonResponse({
#             "date": date,
#             "forecast": weather_data.get(date, "No forecast available")
#         })
# views.py

from django.http import HttpResponse
from django.template import loader
import os

def agricultural_services(request):
    context = {}
    template_path = os.path.join(os.path.dirname(__file__), 'modularized', 'agricultural_services.xml')
    template = loader.get_template(template_path)
    return HttpResponse(template.render(context, request))

def main_and_language(request):
    context = {}
    template_path = os.path.join(os.path.dirname(__file__), 'modularized', 'main_and_language.xml')
    template = loader.get_template(template_path)
    return HttpResponse(template.render(context, request))

def messaging_service(request):
    context = {}
    template_path = os.path.join(os.path.dirname(__file__), 'modularized', 'messaging_service.xml')
    template = loader.get_template(template_path)
    return HttpResponse(template.render(context, request))

def subscription_services(request):
    context = {}
    template_path = os.path.join(os.path.dirname(__file__), 'modularized', 'subscription_services.xml')
    template = loader.get_template(template_path)
    return HttpResponse(template.render(context, request))

def weather_reports(request):
    context = {}
    template_path = os.path.join(os.path.dirname(__file__), 'modularized', 'weather_reports.xml')
    template = loader.get_template(template_path)
    return HttpResponse(template.render(context, request))
