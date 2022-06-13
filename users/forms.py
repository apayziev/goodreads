from django import forms
from users.models import CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name',
                  'last_name', 'email', 'profile_pic')
