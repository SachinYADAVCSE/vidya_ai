from django import forms

# This is the form 
from django.contrib.auth.forms import UserCreationForm

# This is the model of form
# This is the User model in which we can access users from the Database
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


