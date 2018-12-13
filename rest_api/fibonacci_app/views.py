# from django.shortcuts import render
from django.http import JsonResponse
from .mymodules.fibonacci import get_fib_sequence
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from .models import Logs

# caching for a year
@cache_page(31536000)
# required method GET
@require_http_methods(['GET'])
def calc_fibonacci_sequence(request, start_idx=0, end_idx=0):
    response = {
        'data': None,
        'status': 200,
        'error_message': None
    }

    try:
        start_idx = int(start_idx)
        end_idx = int(end_idx)
    except Exception as err:
        response['status'] = 500
        response['error_message'] = str(err)
        return JsonResponse(response)


    if start_idx >= end_idx or start_idx < 0 or end_idx < 0:
        response['status'] = 500
        response['error_message'] = 'Start index should be less than end index and both of them positive numbers'
        return JsonResponse(response)

    try:
        response['data'] = {
            'fibonacci_sequence': get_fib_sequence(start_idx, end_idx),
            'start_idx': start_idx,
            'end_idx': end_idx
        }
    except Exception as err:
        response['status'] = 500
        response['error_message'] = str(err)
        return JsonResponse(response)

    log = Logs(start_idx=start_idx, end_idx=end_idx)
    log.save()


    return JsonResponse(response)


def home(request):
    response = {
        'endpoints': [
            '/fib/<end_idx>/',
            '/fib/<start_idx>/<end_idx>/'
        ]
    }

    return JsonResponse(response)