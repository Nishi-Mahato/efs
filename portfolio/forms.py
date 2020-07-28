from django import forms
from .models import Customer, Stock, Investment, Mails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value','recent_date',)


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class EmailForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Mails
        fields = ('email','subject','message','document',)