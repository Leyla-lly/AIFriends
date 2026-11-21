from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated #退出是需要现在登录状态的

class LogoutView(APIView):
    permission_classes = [IsAuthenticated] #强制必须登录才能访问
    def post(self, request):
        response = Response({
            'result' : 'success'
        })
        response.delete_cookie('refresh_token')
        return response