from rest_framework import status
from rest_framework.response import Response


class IpFilterMiddleware(object):
    def process_request(self, request):
        allowed_ips = ['']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise Response(status=status.HTTP_401_UNAUTHORIZED)
        return None
