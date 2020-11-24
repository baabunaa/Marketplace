from django import forms
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='', 
                        widget=forms.TextInput(attrs={
                                                'placeholder': 'e.g. John_UserName', 
                                                'name' : 'username', 
                                                'required' : 'True'
                                                }))
    password = forms.CharField(label = '',
                        widget=forms.PasswordInput(attrs={
                                                'placeholder': 'Password', 
                                                'name' : 'password', 
                                                'required' : 'True'
                                                }))


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', 
                        widget=forms.TextInput(attrs={
                                                'placeholder': 'e.g. John_UserName', 
                                                'name' : 'username', 
                                                'required' : 'True'
                                                }))
    first_name = forms.CharField(label='First Name', 
                        widget=forms.TextInput(attrs={
                                                'placeholder': 'e.g. John', 
                                                'name' : 'first_name', 
                                                'required' : 'True'
                                                }))
    last_name = forms.CharField(label='Last Name',
                        widget=forms.TextInput(attrs={
                                                'placeholder': 'e.g. Jones', 
                                                'name' : 'last_name', 
                                                'required' : 'True'
                                                }))
    email = forms.EmailField(label='Email', 
                        widget=forms.EmailInput(attrs={
                                                'placeholder': 'Example@email.com', 
                                                'name' : 'email', 
                                                'required' : 'True'
                                                }))
    password = forms.CharField(label='Password',
                        widget=forms.PasswordInput(attrs={
                                                'placeholder': 'pass123', 
                                                'name' : 'password', 
                                                'required' : 'True'
                                                }))
    repeat_password = forms.CharField(label='Repeat Password',
                        widget=forms.PasswordInput(attrs={
                                                'placeholder': 'pass123', 
                                                'name' : 'repeat_password', 
                                                'required' : 'True'
                                                }))
    phone_number = forms.CharField(label='Phone Number',
                        widget=forms.TextInput(attrs={
                                                'placeholder': '363636363', 
                                                'name' : 'phone_number', 
                                                'required' : 'True'
                                                }))