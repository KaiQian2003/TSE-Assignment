from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import DeliveryDriver

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    
class DeliveryDriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = DeliveryDriver
        fields = ['driverID', 'driverName', 'driverHp', 'vehicleDes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding placeholders and CSS classes for styling
        self.fields['driverID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Driver ID'})
        self.fields['driverName'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Driver Name'})
        self.fields['driverHp'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone Number'})
        self.fields['vehicleDes'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description of Vehicle'})

    def clean_driverHp(self):
        # Custom validation for phone number field
        driverHp = self.cleaned_data.get('driverHp')
        # Basic check to ensure it contains only digits
        if not driverHp.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        return driverHp
