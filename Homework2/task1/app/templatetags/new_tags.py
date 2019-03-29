from django import template


register = template.Library()


@register.filter
def gradient(value):
    if value == '-':
        return ''
    else:
        if float(value) < 0:
            return '#1d820f'
        elif 1 <= float(value) <= 2:
            return '#ff5454'
        elif 2 < float(value) <= 5:
            return 'f72c2c'
        elif float(value) > 5:
            return '#ef0707'
        else:
            return ''
