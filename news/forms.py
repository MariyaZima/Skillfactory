from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect


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


