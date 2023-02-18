from django import forms

from .models import Student
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordChangeForm,PasswordResetForm
from django.utils.translation import gettext as _



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Student
class StudentDetailsForm(forms.ModelForm):
    class Meta():
        model = Student
        fields =['first_name','last_name','email','phone']
        widgets= {'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'phone':forms.TextInput(attrs={'class':'form-control'}),
                 }
class StudentRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm-Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta():
        model = User
        fields = ['username','email','password1','password2']
        labels ={'email','Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"),max_length=200,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-controle'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form_controle'}))
    new_password2=forms.CharField(label=_("confirm new password"),max_length=200,strip=False,widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password','class':'form-controle'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

# from django import forms
# from .models import Email

# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = Email
#         fields = ('email',)



    



