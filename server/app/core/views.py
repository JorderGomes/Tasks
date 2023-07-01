from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer 

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer