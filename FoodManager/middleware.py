from django.conf import settings
from authentication.serializers import AccessToken
from rest_framework.response import Response
class CheckBlackListMiddleWare:
    def __init__(self, get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        response=self.get_response(request)
        # print(request.META.get('HTTP_AUTHORIZATION'))
        access=request.META.get('HTTP_AUTHORIZATION')
        
        if access:
            access=access.split()
            # print(access[1])
            if AccessToken(access[1]).check_blacklist():
                exit()
        return response

    def process_exception(self, request, response):
        pass