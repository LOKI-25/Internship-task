import jwt
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1] if 'HTTP_AUTHORIZATION' in request.META else None

        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = payload.get('user_id')

                try:
                    user = User.objects.get(id=user_id)
                    request.user = user
                except User.DoesNotExist:
                    pass
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.DecodeError:
                return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)
        return response
