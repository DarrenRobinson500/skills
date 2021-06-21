from django import template
from app.models import Colour

register = template.Library()
@register.simple_tag
def colour_nav(request):
    try:
        colour = Colour.objects.filter(active=True)[0]
        result = colour.nav
    except:
        result = "563D7C"
    return result