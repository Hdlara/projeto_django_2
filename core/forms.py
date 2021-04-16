from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', min_length=3, max_length=100)
    email = forms.EmailField(label='E-mail', min_length=6, max_length=100)
    celular = forms.CharField(label='Celular', min_length=8, max_length=13)
    assunto = forms.CharField(label='Assunto', min_length=5, max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        celular = self.cleaned_data['celular']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\nE-mail: {email}\nCelular: {celular}\nMessagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br', 'outro@seuemail.com'],
            headers={'Reply-To': email}
        )
        mail.send()
