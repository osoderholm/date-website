from django.utils.text import slugify
from django.conf import settings
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class LangMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
        try:
            pass
            # TODO This is borked as of Django 4.0 but it doesn't seem like it's in use
            # See: https://stackoverflow.com/questions/2605384/how-to-explicitly-set-django-language-in-django-session
            # lang = request.session[translation.LANGUAGE_SESSION_KEY]
            # if lang in [settings.LANG_SWEDISH, settings.LANG_FINNISH] and lang is not None:
            #    request.LANG = lang
        except KeyError:
            pass

        translation.activate(request.LANG)
        request.LANGUAGE_CODE = request.LANG

def slugify_max(text, max_length=50):
    slug = slugify(text)
    if len(slug) <= max_length:
        return slug
    trimmed_slug = slug[:max_length].rsplit('-', 1)[0]
    if len(trimmed_slug) <= max_length:
        return trimmed_slug
    # First word is > max_length chars, so we have to break it
    return slug[:max_length]
