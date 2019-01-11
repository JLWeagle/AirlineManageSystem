from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
                        label='用户名',
                        max_length=100,
                        min_length=5,
                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='电子邮箱', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
                            label="密码",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
                            label="确认密码",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('该邮箱帐号已被占用')
        return email

    # def clean_password1(self):
    #     # this will raise a key error because it references password2 field
    #     # which is ran AFTER password1 validation
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password1 Does Not Match Password2')
    #     return p1

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password2 Does Not Match Password1')
    #     return p2

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError('密码不匹配')
