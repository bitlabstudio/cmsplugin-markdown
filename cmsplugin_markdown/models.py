from django.db import models

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class MarkdownPlugin(CMSPlugin):
    markdown_text = models.TextField(max_length=8000)

    def __str__(self):
        text = self.markdown_text
        return (text[:50] + '...') if len(text) > 53 else text
