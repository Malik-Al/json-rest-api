import json
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt              # Декоратор @csrf_exempt обозначает, что для этого представления Django не будет проверять наличие csrf-токена при POST-запросах.
def json_echo_view(request, *args, **kwargs):
    data = None
    if request.body:
        data = json.loads(request.body)
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
        'content': data
    }

    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response
