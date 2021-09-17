from django import forms

from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    comentario = forms.CharField(label='Teste uppercase', widget=forms.TextInput(
        attrs={'size': '80', 'placeholder': 'Digite o comentário', 'style': "text-transform: uppercase;"}))
    numeros = forms.IntegerField(label='Teste só números', required=False, widget=forms.NumberInput(
        attrs={'type': 'number', 'onkeypress': 'return soNumero(event)'}))
    numeros2 = forms.IntegerField(
        label='Teste de validator que agora ta sem validator', help_text='Preencha com numero porra')
    numeros3 = forms.IntegerField(label='Campo numérico sem a setinha')
    readonly = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(attrs={'readonly': ''}))

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}\n"

        mail = EmailMessage(
            subject='E-mail enviado pelo Django',
            body=conteudo,
            from_email='contato@meudominio.com',
            to=['contato@meudominio.com', 'outroemail@meudominio'],
            headers={'Reply-to': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco', 'estoque', 'imagem']
