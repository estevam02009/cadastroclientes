from rest_framework import serializers
from api.models import CadastroCliente

class CadastroClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = '__all__'