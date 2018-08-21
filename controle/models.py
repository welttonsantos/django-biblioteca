from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length = 255)
    cpf = models.CharField(max_length = 255)
    telefone = models.CharField(max_length = 255)

    def __str__(self):
        return '{} ({}) '.format(self.nome , self.cpf)


class Funcionario(models.Model):

    nome= models.CharField(max_length = 255)
    cpf= models.CharField(max_length = 255)
    telefone= models.CharField(max_length = 255)
    cargo = models.CharField(max_length = 200)

    def __str__(self):
       return '{} , {}'.format(self.nome , self.cargo)


class Livros(models.Model):

    nome = models.CharField(max_length = 255)
    descricao = models.CharField(max_length = 200)
    quantidade = models.CharField(max_length = 255)
    autor = models.CharField(max_length = 255)

    def __str__(self):
       return '{} , {} , {}'.format( self.nome , self.descricao ,self.autor)

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE)
    funcionario = models.ForeignKey(Funcionario,on_delete = models.CASCADE)
    livro = models.ForeignKey(Livros,on_delete = models.CASCADE)
    emprestimo= models.BooleanField(default = False)

    def __str__(self):
       return '{} , {} , {}, {}'.format(self.id, self.cliente , self.funcionario , self.livro , self.emprestimo)
