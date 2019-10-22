from django import forms
from members.models import MyUser



from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    podio_code = forms.CharField(label="Podio ID", widget=forms.TextInput(attrs={'class': 'masterclass'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MyUser
        fields = ('podio_code', 'password', 'email', 'first_name', 'last_name', 'department', 'post', 'leader')


class UserFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserFormEdit, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = MyUser
        exclude = ('password', 'last_login', 'is_working')