import modeltranslation 
from modeltranslation.translator import TranslationOptions, translator,register

from.models import *

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('description',)