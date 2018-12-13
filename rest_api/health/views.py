from django.http import JsonResponse
from .mymodules.health import SRM, endpointhealth
from django.views.decorators.cache import cache_page

@cache_page(31536000)
def health(request):
    
    data = SRM.get_datas()
    data['service_health'] = []

    path = request.get_host()
    
    try:
        data['service_health'].append(endpointhealth(path + '/fib/'))
    except Exception as err:
        data['service_health'].append(str(err))

    try:
        data['service_health'].append(endpointhealth(path + '/fib/50/'))
    except Exception as err:
        data['service_health'].append(str(err))

    try:
        data['service_health'].append(endpointhealth(path + '/fib/5/60/'))
    except Exception as err:
        data['service_health'].append(str(err))

    return JsonResponse(data)