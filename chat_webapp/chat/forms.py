from django import forms
from .models import Message, User, Comment


class UserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['name']
    widgets = {
        'name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your name'}
        ),
    }


class MessageForm(forms.ModelForm):

  class Meta:
    model = Message
    fields = ['text','title']
    widgets = {
        'text': forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 3,
            }
        ),
        'title': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter your message',
                        'rows': 3,
                    }
        )
    }


class MessageEditForm(forms.ModelForm):

  class Meta:
    model = Message
    fields = ['text', 'title']
    widgets = {
        'text': forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Edit your message',
                'rows': 3,
            }
        ),
        'title': forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'placeholder': 'Enter your message',
                                'rows': 3,
                            }
                )
    }

class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ['text']
    widgets = {
        'text': forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 3,
            }
        ),
    }

class CommentEditForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ['text']
    widgets = {
        'text': forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Edit your message',
                'rows': 3,
            }
        ),
    }