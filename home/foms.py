from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SearchForm(forms.Form):
    query = forms.CharField(label='Search ', max_length=100)


#    catid= forms.IntegerField()

class SginupForm(UserCreationForm):
    username = forms.CharField(label='User Name ', max_length=100)
    email = forms.CharField(label='Email ', max_length=100)
    first_name = forms.CharField(label='First Name :', help_text='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name :', help_text='Last Name', max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


""""  widgets = {

            'username': TextInput(attrs={'class': 'input', 'placeholder': 'Kullanıcı Adı'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'Ad'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Soyad'}),
            'password1': TextInput(attrs={'class': 'input', 'placeholder': 'Şifre'}),
            'password2': TextInput(attrs={'class': 'input', 'placeholder': 'Şifre'}),
        }"""
