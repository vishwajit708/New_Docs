from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    password1=forms.CharField(label="Repeat Password",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('email','first_name')

    def clean_password2(self):
        cd=self.clean_data
        if cd["password"]!=cd["password1"]:
            raise forms.validationError("password don't match ")
        return cd["password"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
