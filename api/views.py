from divers.models import Divers
from rest_framework import viewsets
from rest_framework.views import APIView
from api.serializer import DiverSerializer
from rest_framework import authentication, permissions,routers
from rest_framework.response import Response
class divers(viewsets.ModelViewSet):
    queryset = Divers.objects.all()
    serializer_class = DiverSerializer
  




