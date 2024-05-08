from django.http import JsonResponse

def users(request):
    if request.method == 'GET':
        user = {
            'id': 1,
            'name': 'Sam M. Martin',
            'work': 'Developer'
        }

        return JsonResponse(user)