from django import template
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def time_since_publish(created_date):
    now = timezone.now()
    diff = now - created_date

    if diff.days == 0:
        if diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f"{minutes} minutes ago"
        else:
            hours = diff.seconds // 3600
            return f"{hours} hours ago"
    elif diff.days == 1:
        return "Yesterday"
    else:
        return f"{diff.days} days ago"