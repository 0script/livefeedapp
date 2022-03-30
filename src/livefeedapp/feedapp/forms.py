from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Post
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=UserCreationForm.Meta.fields+('tel',)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,
        required=True,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Type your username',
                'type':'text',
                'class':'input',
            }
        )
    )
    password=forms.CharField(label='Password', widget=forms.PasswordInput)


class PostMsgForm(forms.Form):
    
    text=forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Include message here',
                'type':'input',
                'class':'message',

            }
        )
    )


class PostForm(forms.ModelForm):
    
    text=forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Include message here',
                'type':'input',
                'class':'message',

            }
        )
    )

    user=forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model=Post
        fields=('text',)


# class CustomUserCreationForm(UserCreationForm):

#     username=forms.CharField(max_length=150,
#         required=True,
#         label='Username',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':'Type your username',
#                 'type':'text',
#                 'class':'input',
#             }
#         )
#     )

#     email=forms.EmailField(
#         required=False,
#         label='Email',
#         widget=forms.EmailInput(
#             attrs={
#                 'placeholder':'Type Your email',
#                 'type':'text',
#                 'class':'email',
#             }
#         )
#     )

#     tel=forms.CharField(max_length=150,
#         required=True,
#         label='Tel',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':'Your Phone Number',
#                 'type':'text',
#                 'class':'input',
#             }
#         )
#     )


#     # tel=forms.RegexField(
#     #     regex=r'^\+?1?\d{9,15}$',
#     #     required=False,
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             'placeholder':'Your Phone Number',
#     #             'type':'text',
#     #             'class':'input',
#     #         }
#     #     )
#     # )

#     class Meta:
#         model = User
#         fields = ('username','email','tel','password')

#     def username_clean(self):
#         username=self.cleaned_data['username'].lower()
#         new=User.objects.filter(username=username)
        
#         if new.count():
#             raise ValidationError('Username Already Exist')
#         return username

#     def email_clean(self):
#         email=self.cleaned_data['email'].lower()
#         new=User.objects.filter(email=email)
#         if new.count():
#             raise ValidationError('Email Already Exist')
#         return email
    
#     def tel_clean(self):
#         tel=self.cleaned_data['tel'].lower()
#         new=User.objects.filter(tel=tel)
#         if new.count():
#             raise ValidationError('Phone number already exist')
#         return tel

#     # def password1_clean(self):
#     #     password1=self.cleaned_data['password1']
#     #     password2=self.cleaned_data['password2']

#     #     if password1 and password2 and password1!=password2:
#     #         raise ValidationError('Password do not match')
#     #     return password2

#     def save(self,commit=True):
#         user=CustomUser.objects.create_user(
#             self.cleaned_data['username'],
#             self.cleaned_data['email'],
#             self.cleaned_data['tel'],
#             self.cleaned_data['passwrod']
#         )

#         return user