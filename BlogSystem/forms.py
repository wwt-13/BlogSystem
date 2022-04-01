from django import forms
from django.forms import ModelForm, widgets
from .models import User, Article
from django.core.exceptions import ValidationError
import re


class RegisterForm(forms.Form):
    name = forms.CharField(
        label="name",  # 显示的就是表单前面的那个东西
        max_length=50,
    )
    password1 = forms.CharField(
        label="password1",
    )
    password2 = forms.CharField(
        label="password2",
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.match('^[a-zA-Z0-9]{,12}$', name) is None:
            raise ValidationError(
                "Please enter your name consisting of numbers and letters only!")
        elif User.objects.filter(name=name).exists():
            raise ValidationError("This username is already in use!")
        else:
            return name

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if re.match('^(?=.*[0-9])(?=.*[a-zA-Z])(.{8,16})$', password1) is None:
            raise ValidationError(
                "Please enter your password in a correct format!")
        else:
            return password1

    def clean(self):  # 多个输入之间的检测必须使用全局钩子解决
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError(
                "The two entered passwords are not the same!")
        else:
            return self.cleaned_data

    def __init__(self, *args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input input--text','type':'text'})

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input input--text','type':'text'})

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):

        super(ArticleForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Input your article title here.'})


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):

        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
