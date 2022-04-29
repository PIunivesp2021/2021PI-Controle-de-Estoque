from django.forms import ModelForm
from app.models import Controle


class ControleForm(ModelForm):
    class Meta:
        model = Controle
        fields = ['Empenho', 'Nota_Fiscal', 'Material', 'Obs', 'Data_Envio']
