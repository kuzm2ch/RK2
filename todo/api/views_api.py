from rest_framework import viewsets
from rk.models import Computer, Program
from .serializers import ComputerSerializer, ProgramSerializer
class ComputerListAPIView(viewsets.ModelViewSet):

    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()

class ProgramListAPIView(viewsets.ModelViewSet):

    serializer_class = ProgramSerializer
    queryset = Program.objects.all()