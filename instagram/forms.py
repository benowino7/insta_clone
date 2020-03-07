from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Comment

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Please use a valid email address')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude=['likes', 'slug','profile', 'posted_at']

class CommentForm(forms.ModelForm):
   class Meta:
       model=Comment
       exclude=['comment_pic','posted_by']
    # class meta:defines such things as available permissions, associated database table name, whether the model is abstract or not, singular and plural versions of the name.