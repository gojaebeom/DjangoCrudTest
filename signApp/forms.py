from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']  # 로그인 시에는 이메일과 비밀번호만 입력 받는다.
