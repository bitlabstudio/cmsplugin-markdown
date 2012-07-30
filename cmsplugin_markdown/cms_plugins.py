"""Implementation of CMSPluginBase class for ``cmsplugin-markdown``."""
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cmsplugin_markdown.models import MarkdownPlugin


class MarkdownCMSPlugin(CMSPluginBase):
    model = MarkdownPlugin
    name = _('Markdown')
    render_template = 'cmsplugin_markdown/markdown.html'
    change_form_template = 'cmsplugin_markdown/change_form.html'

    def render(self, context, instance, placeholder):
        context['text'] = instance.markdown_text
        return context


plugin_pool.register_plugin(MarkdownCMSPlugin)
