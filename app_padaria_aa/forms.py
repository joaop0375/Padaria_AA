from django import forms
from app_padaria_aa.models import Cliente, Reclamacao, Encomenda, Pedido, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']

class ReclamacaoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    class Meta:
        model = Reclamacao
        fields = ['cliente', 'descricao' ]

class EncomendaForm(forms.ModelForm):
    class Meta:
        model = Encomenda
        fields = ['cliente', 'quantidade']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['encomenda', 'produto', 'quantidade']
    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        # Adicione uma opção vazia para a encomenda, você pode personalizar isso conforme necessário
        self.fields['encomenda'].queryset = Encomenda.objects.all().order_by('id').reverse()
        self.fields['encomenda'].choices = [('', 'Pão')] + list(self.fields['encomenda'].choices)
        self.fields['encomenda'].choices = [('', '---------')] + list(self.fields['encomenda'].choices)
    