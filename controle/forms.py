from django import forms
from .models import Cliente
from .models import Funcionario
from .models import Livros
from .models import Processo


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields="__all__"


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model=Funcionario
        fields="__all__"

class LivrosForm(forms.ModelForm):
    class Meta:
        model=Livros
        fields="__all__"

class ProcessoForm(forms.ModelForm):
    class Meta:
        model=Processo
        fields="__all__"

class BuscaForm(forms.Form):
    nome = forms.CharField(max_length=255)
