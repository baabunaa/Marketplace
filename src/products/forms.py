from django import forms
from products.models import Post

CATEGORIES = [
    ('HT', 'Home Technics'),
    ('EL', 'Electronics'),
    ('SP', 'Sports'),
    ('MA', 'Music & Art')
]


class PostForm(forms.Form):
    name = forms.CharField(label='Name', 
                        widget=forms.TextInput(attrs={
                                                'name' : 'name', 
                                                'required' : 'True'
                                                }))
    price = forms.CharField(label='Price', 
                        widget=forms.NumberInput(attrs={
                                                'placeholder': 'Price in euros', 
                                                'name' : 'price', 
                                                'required' : 'True'
                                                }))
    description = forms.CharField(label='Description', 
                        widget=forms.TextInput(attrs={
                                                'placeholder': 'Describe the details', 
                                                'name' : 'description'
                                                }))
    category = forms.ChoiceField(label='Category', choices=CATEGORIES)
    image = forms.ImageField(label='')

