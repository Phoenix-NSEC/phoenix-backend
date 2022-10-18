from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class Ping(APIView):
    def get(self, request, format=None):
        return Response({"message": "pong!"})
    
class Home(APIView):
    def get(self, request, format=None):
        return Response("Hello World!")