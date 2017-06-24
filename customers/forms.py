from django import forms
from customers.models import User, Courses
from users import settings


class UserAdminForm(forms.ModelForm):
    user_permissions = forms.SelectMultiple(
        attrs={
            'class': 'select2'
        }
    )

    class Meta:
        model = User
        exclude = ('last_login', 'password')



class SingUpForm(forms.ModelForm):
    email = forms.EmailField(
        label='E-Mail',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail.com'})
    )
    password = forms.CharField(
        label='Password',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    name = forms.CharField(
        label='Name',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    phone = forms.CharField(
        label='Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Phone'})
    )
    mobile_phone = forms.CharField(
        label='Mobile Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Phone'})
    )

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'phone', 'mobile_phone')
