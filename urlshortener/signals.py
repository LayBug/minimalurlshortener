from django.db.models.signals import (post_save,pre_save)
from random import randint
from .models import ShortUrl

alphabets_list = list(map(chr, range(97, 123)))

def generate_suffix():
    suffix_list = []
    for i in range(7):
        x = randint(1,7)
        suffix_list.append(alphabets_list[x])
    suffix = ''.join(suffix_list)
    return suffix

def generate_short_url(sender, instance, **kwargs):
    if instance.suggested_url_suffix:
        suffix = instance.suggested_url_suffix
        if ' ' in suffix:
            raise ValueError
        instance.generated_url= "http://localhost:8000/" + suffix
        instance.slug = instance.suggested_url_suffix
    else:
        suffix = generate_suffix()
        instance.generated_url = "http://localhost:8000/" + suffix
        instance.slug = suffix

pre_save.connect(generate_short_url, sender = ShortUrl)


