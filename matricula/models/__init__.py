from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

CLASSE_CHOICE = (
    (1, '1ª'),
    (2, '2ª'),
    (3, '3ª'),
    (4, '4ª'),
    (5, '5ª'),
    (6, '6ª'),
    (7, '7ª'),
    (8, '8ª'),
    (9, '9ª'),
    (10, '10ª'),
    (11, '11ª'),
    (12, '12ª'),
)

SEXO = [    
    ('masculino', _('Masculino')),
    ('femenino', _('Femenino')),
    ('outro', _('Outro'))
]

from .Alunos import Aluno
from .Boletim import DadosEncaregado
from .Boletim import DadosPessoais