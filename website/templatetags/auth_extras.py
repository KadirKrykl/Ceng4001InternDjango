from django import template
from django.contrib.auth.models import Group 
from django import template
from django.urls import translate_url

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.filter(name='update_variable')
def update_variable(data, value):
    data = value
    return data

@register.simple_tag(takes_context=True)
def change_lang(context, lang: str, *args, **kwargs):
    path = context['request'].path
    return translate_url(path, lang)