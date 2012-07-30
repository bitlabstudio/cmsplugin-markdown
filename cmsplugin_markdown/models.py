from django.db import models

from cms.models import CMSPlugin


class MarkdownPlugin(CMSPlugin):
    markdown_text = models.TextField(max_length=8000)
