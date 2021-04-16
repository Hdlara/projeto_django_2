from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    telefone = forms.CharField(label='Celular')
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())