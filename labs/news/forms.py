from .models import Articles
from django.forms import ModelForm, fields, TextInput, DateTimeInput, Textarea
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Дата публикации'
            }),
        }


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user