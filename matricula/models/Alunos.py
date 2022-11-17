
from matricula.models import *


class Aluno(models.Model):
    nome=models.ForeignKey('DadosPessoais', on_delete=models.CASCADE, blank=True, null=True, default=1)
    contacto=PhoneNumberField(region="MZ")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    classe=models.IntegerField(choices=CLASSE_CHOICE, default=1)
    nr_de_senha=models.IntegerField()
    senha_passada=models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.nome)