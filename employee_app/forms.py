from django import forms
from phonenumber_field.formfields import PhoneNumberField
from manager_app.models import Users


class EmployeeRegForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Full Name', 'class': "form-control form-control-sm"}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Last Name', 'class': "form-control form-control-sm"}), max_length=50)
    company = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Company', 'class': "form-control form-control-sm"}), max_length=50, required=False)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City', 'class': "form-control form-control-sm"}), max_length=50, required=False)
    dob = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': "form-control form-control-sm"}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password', 'class': "form-control form-control-sm"}), required=False)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': ' Email', 'class': "form-control form-control-sm"}),
        required=False)
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': ' Address', 'cols': 20, 'rows': 5,
                                     'class': "form-control form-control-sm"}), required=False)
    mobile = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': ' Mobile No', 'class': "form-control form-control-sm"}),
        help_text='Must include international prefix - e.g. +1 123 456 78910')
    employee_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}), required=True)

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'company', 'city', 'dob', 'password', 'email', 'address', 'mobile',
                  'employee_id')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = Users.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('Email is already registered')
        return email
