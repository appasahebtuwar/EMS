from django import forms
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from manager_app.models import Users


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' First Name', 'class': "form-control form-control-sm"}), max_length=50, required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Last Name', 'class': "form-control form-control-sm"}), max_length=50, required=True)
    company = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Company', 'class': "form-control form-control-sm"}), max_length=55, required=False)
    dob = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': "form-control form-control-sm"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password', 'class': "form-control form-control-sm"}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': ' Email', 'class': "form-control form-control-sm"}), required=True)
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': ' Address', 'cols': 20, 'rows': 5,
                                     'class': "form-control form-control-sm"}), required=False)
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'company', 'dob', 'password', 'email', 'address')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = Users.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('Email is already registered')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long!')
        return password

# # login form
# class UserLoginForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#
#     def clean(self, *args, **kwargs):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         if email and password:
#             user = auth.authenticate(email=email, password=password)
#             if not user:
#                 raise forms.ValidationError("user dose not exist")
#             pwd = Users.objects.get(email=email)
#             if not pwd.check_password(password):
#                 raise forms.ValidationError("invalid password")
#         return self.cleaned_data


# login form
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            print(user)
            if not user:
                raise forms.ValidationError("user does not exist")
            pwd = Users.objects.get(email=email)
            if not pwd.check_password(password):
                raise forms.ValidationError("invalid password")
        return self.cleaned_data
