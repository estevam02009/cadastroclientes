from django.db import models
import uuid

class CadastroCliente(models.Model):
    BAIRRO_CHOICES = [
        ('leandro_bezerra', 'Leandro Bezerra'), ('alto_sao_severino', 'Alto São Severino'), ('centro', 'Centro'),
        ('sebastiao_maltez', 'Sebastião Maltêz'), ('nestor_fernandes', 'Nestor Fernandes'),
        ('aroudo_maia', 'Aroudo Maia'), ('guiido_gurgel', 'Guido Gurgel'), ('nico_fernandes', 'Nicó Fernandes'),
        ('nova_caraubas', 'Nova Caraúbas'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    rua = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    numero = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        null=False,
        blank=True
    )
    bairro = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=BAIRRO_CHOICES
    )
    data_cadastro = models.DateField(
        null=False,
        blank=False,
    )
