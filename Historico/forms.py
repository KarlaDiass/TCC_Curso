from django import forms
from django.forms import ModelForm
from .models import HistoricoConsultas


class HistoricoConsultasForm(forms.ModelForm):
    class Meta:
        model = HistoricoConsultas
        fields = ['lugar', 'data', 'receita', 'atestado', 'fk_usuario_historico_consulta']