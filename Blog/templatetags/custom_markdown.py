#coding=utf-8
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
__author__ = 'zjutK'
import markdown



register=template.Library()#自定义filter必须加上

@register.filter(is_safe=True)#注册template
@stringfilter   #希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.fenced_code','markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))