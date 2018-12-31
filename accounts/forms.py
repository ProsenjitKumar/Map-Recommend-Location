from django import forms
from django.contrib.auth.models import User
from .models import UserAccount


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_login(self):
    #     if self.username and self.password:
    #         raise forms.ValidationError("Password or Email Incorrect.")


class RegisterForm(forms.ModelForm):
    # """A form for creating new users. Includes all the required
    # fields, plus a repeated password."""
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('user', 'profile_pic', 'birth_date')
    #
    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     user.active = True # send for admin approval if False
    #     if commit:
    #         user.save()
    #     return user


