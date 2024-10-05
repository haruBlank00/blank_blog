import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdownify")
def markdownify(text):
    """Converts markwon text to HTML"""
    return mark_safe(markdown.markdown(text, extensions=["markdown.extensions.fenced_code"]))
