from django import template
from datetime import datetime
import random

register = template.Library()



@register.filter()
def censor(text):
   bad_words = ['рыгнул', 'бла']
   for word in bad_words:
      if word in text.lower():
         text = text.replace(word, '***')
   return text



@register.simple_tag()
def current_time(format_string='%b %d %Y'):
   return datetime.utcnow().strftime(format_string)