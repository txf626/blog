"""__author__=txf"""
from django import forms

from backblog.models import User


class UserForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=2,required=True,
                               error_messages={'required': '用户名必填', 'max_length': '不能超过长度10',
                                               'min_length': '长度不能小于2'})

    userpwd = forms.CharField(max_length=18,min_length=6,required=True,error_messages={'pw1':'密码必填',
                                                                                       'min_length':'密码长度不能小于6'})

    def clean(self):
        name = self.cleaned_data.get('username')
        user = User.objects.filter(name=name).first()

        if not user:
            raise forms.ValidationError({'username':'该用户不存在'})

        return self.cleaned_data