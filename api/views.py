from django.shortcuts import render
from api.serializer import CadastroClienteSerializer
from rest_framework import viewsets, permissions
from api.models import CadastroCliente


class CadastroClienteViewSet(viewsets.ModelViewSet):
    queryset = CadastroCliente.objects.all()
    serializer_class = CadastroClienteSerializer
    permission_classes = [permissions.IsAuthenticated]