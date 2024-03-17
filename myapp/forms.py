from django import forms

from .models import Product


class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.ru') or email.endswith('mail.ru')):
            raise forms.ValidationError('Используйте почту vk.ru или mail.ru')
        return email


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField(max_length=50, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    count = forms.IntegerField()
    image = forms.ImageField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'count', 'image')
