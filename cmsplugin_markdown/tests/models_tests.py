"""Tests for the models of the ``cmsplugin_markdown`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class MarkdownPluginTestCase(TestCase):
    """Tests for the ``MarkdownPlugin`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('cmsplugin_markdown.MarkdownPlugin')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))
