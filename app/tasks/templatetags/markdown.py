from django import template
from markdown import markdown as md2html

register = template.Library()


@register.filter
def markdown(text):
    return md2html(text.replace("\n", "\n\n"))
