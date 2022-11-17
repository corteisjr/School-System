from matricula.models import *

class DadosPessoais(models.Model):
    processo_nr = models.IntegerField(default=0)
    nome_completo = models.CharField(max_length=50, help_text='Nome completo')
    sexo = models.CharField(choices=SEXO, max_length=20, blank=True, null=True,)
    nome_do_pai = models.CharField(max_length=50, help_text='Nome do Pai')
    nome_da_mae = models.CharField(max_length=50, help_text='Nome da mãe')
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    local_nascimento = models.CharField(max_length=50, help_text='Local de nascimento')
    distrito = models.CharField(max_length=50, help_text='Distrito')
    provincia = models.CharField(max_length=50, help_text='Província')
    bi_nr = models.IntegerField(default=None, null=True, blank=True)
    cedula_nr = models.IntegerField(default=None, null=True, blank=True)
    emissao = models.CharField(max_length=50, help_text='Emissao')
    morada = models.CharField(max_length=50, help_text='Morada')
    bairro = models.CharField(max_length=50, help_text='Bairro')
    telefone = PhoneNumberField(region="MZ")
    
    def __str__(self):
        return '{}'.format(self.nome_completo)
    
class DadosEncaregado(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome do encarregado')
    profissao = models.CharField(max_length=50, help_text='Profissão')
    local_de_trabalho = models.CharField(max_length=50, help_text='Local de Trabalho')
    residencia = models.CharField(max_length=50, help_text='Residencia')
    telefone = PhoneNumberField(region='MZ')
    email = models.EmailField(max_length=100, help_text='Email')
    ano_letivo = models.DateField()
    frenquentou = models.IntegerField(choices=CLASSE_CHOICE, default=1)
    turma = models.CharField(max_length=50, help_text='Turma', default=None)
    numero = models.IntegerField(default=None, null=True, blank=True)
    escola = models.CharField(max_length=100, help_text='Escola')
    data = models.DateField()
    
    