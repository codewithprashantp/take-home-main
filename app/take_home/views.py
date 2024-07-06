from django.http import JsonResponse
from .weather_utility import get_weather_data
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view


@api_view()
def check_weather(request):
    city = request.GET.get('city')
    if not city:
        raise ValidationError({"Message": "City Parameter is needed"})
    return JsonResponse(
        get_weather_data(city)
    )
