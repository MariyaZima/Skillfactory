from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'content',
            'many_to_many_relation',
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        if content is not None and len(content) < 20:
            raise ValidationError({
                "content": "Описание не может быть менее 20 символов."
            })

        title = cleaned_data.get("title")
        if title == content:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )
        return cleaned_data


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })



