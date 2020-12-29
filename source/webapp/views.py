import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

#
# @csrf_exempt              # Декоратор @csrf_exempt обозначает, что для этого представления Django не будет проверять наличие csrf-токена при POST-запросах.
# def json_echo_view(request, *args, **kwargs):
#     data = None
#     if request.body:
#         data = json.loads(request.body)
#     print(data.get('key'))    # вывести ключ key
#     answer = {
#         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         'method': request.method,
#         'content': data
#     }
#
#     answer_as_json = json.dumps(answer)
#     response = HttpResponse(answer_as_json)
#     response['Content-Type'] = 'application/json'
#     return response


@csrf_exempt
def json_add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) + int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response

@csrf_exempt
def json_subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) - int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response


@csrf_exempt
def json_multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) * int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response

@csrf_exempt
def json_divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A')
            B = data.get('B')
            try:
                answer = {
                    'answer': int(A) / int(B)
                }
                return JsonResponse(answer)
            except:
                response = JsonResponse({'error': 'Bad request'})
                response.status_code = 400
                return response
