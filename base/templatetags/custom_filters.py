from django import template

register = template.Library()

@register.filter
def is_pdf(value):
    return value.lower().endswith('.pdf')
@register.filter
def is_vid(value):
    return value.lower().endswith('.mp4')
@register.filter
def is_txt(value):
    return value.lower().endswith('.txt')
@register.filter
def is_img(value):
    return value.lower().endswith(('.jpg', '.jpeg', '.png', 'pdf'))

