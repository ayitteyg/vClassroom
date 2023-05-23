from django import forms 
from .models import *
from django.contrib.auth.models import User




class userform(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name","contact", "Class", "email")
    
    def clean(self):
        cleaned_data = super(userform, self).clean()
        return cleaned_data



class loginform(forms.Form):
    username = forms.CharField(max_length=30, label='',widget=forms.TextInput (attrs={'placeholder': 'username'}))
    password = forms.CharField(label=(""), widget=forms.PasswordInput (attrs={'placeholder': 'password'}))
    def clean(self):
        cleaned_data = super(loginform, self).clean()
        return cleaned_data
    


class UserCreationForm(forms.ModelForm):

    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'password_length': ("password short, must be 5 character or more."),
        'password_type_nmb': ("password must have at least an alphabet "),
        'password_type_alph': ("password must have at least a number."),
    }
    password1 = forms.CharField(label=(""),
        widget=forms.PasswordInput (attrs={'placeholder': 'Choose a password'}))
    password2 = forms.CharField(label=(""),
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}),
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
       
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        
        if password1 and password2 and len(password1 or password2) < 5:
            raise forms.ValidationError(
                self.error_messages['password_length'],
                code='password_length',
            )


        if password1.isnumeric() or password2.isnumeric() :
            raise forms.ValidationError(
                self.error_messages['password_type_nmb'],
                code='password_type_nmb',
            )
        

        if password1.isalpha() or password2.isalpha() :
            raise forms.ValidationError(
                self.error_messages['password_type_alph'],
                code='password_type_alph',
            )

        return password2
       

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
