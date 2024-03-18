from django import template

register = template.Library()


@register.filter()
def censor(new):
    return ' '.join('*' * len(i) if len(i) > 4 else i for i in new.split())
