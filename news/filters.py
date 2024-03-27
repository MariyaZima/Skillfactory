from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    data_in = DateFilter(field_name='datetime',
                         widget=forms.DateInput(attrs={'type': 'date'}),
                         label='Дата',
                         lookup_expr='date__gte',
                         )

    class Meta:
        model = Post
        fields = {
            'title': ['exact'],
            'author': ['exact'],

        }
