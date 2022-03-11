import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from members.models import Member
from django.utils.translation import gettext_lazy as _


class MemberAutenticationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Niepoprawne hasło lub email.')


class RegistrationForm(UserCreationForm):
    gender_choices = (
        ('M', 'Mężczyzna'), 
        ('K', 'Kobieta'),
    )

    email = forms.EmailField(max_length=60, label='E-mail')
    gender = forms.ChoiceField(choices=gender_choices, label='Płeć')
    # consent = forms.BooleanField(required=True, label = "Wyrażam zgodę na warunki regulaminu.")

    class Meta:
        model = Member
        fields = ('email', 'username', 'gender', 'password1', 'password2')
        labels = {
            'username': _('Nazwa użytkownika'),
            'tak': _('Akceptuję Regulamin')
        }

class UpdateUserForm(forms.ModelForm):
    gender_choices = (
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
    )
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=gender_choices, label='Płeć')

    class Meta:
        model = Member
        fields = ['username', 'email', 'gender']