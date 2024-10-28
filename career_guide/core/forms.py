
from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feedback
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email address', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'password1': 'Password',
            'password2': 'Password confirmation',
        }
        help_texts = {
            'username': 'Enter your username',
            'password1': None,  # Removes password validation help text
            'password2': 'Enter the same password as before, for verification',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feedback
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email address', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'password1': 'Password',
            'password2': 'Password confirmation',
        }
        help_texts = {
            'username': 'Enter your username',
            'password1': None,  # Removes password validation help text
            'password2': 'Enter the same password as before, for verification',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'feedback_text', 'phone_number']


from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['qualification', 'age', 'location']



