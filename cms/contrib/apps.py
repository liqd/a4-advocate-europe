from django.apps import AppConfig


def InlineStyleElementHandler__handle_endtag(self, name, state, contentstate):
    inline_style_range = state.current_inline_styles.pop()
    assert inline_style_range.style == self.style
    try:
        inline_style_range.length = (
            len(state.current_block.text) - inline_style_range.offset
        )
    except AttributeError:
        inline_style_range.length = inline_style_range.offset


def BlockElementHandler__handle_endtag(self, name, state, contentState):
    state.current_block = None


class Config(AppConfig):
    name = 'cms.contrib'
    label = 'cms_contrib'

    def ready(self):
        from wagtail.admin.rich_text.converters.html_to_contentstate import (
            InlineStyleElementHandler,
            BlockElementHandler
        )

        InlineStyleElementHandler.handle_endtag = (
            InlineStyleElementHandler__handle_endtag
        )
        BlockElementHandler.handle_endtag = (
            BlockElementHandler__handle_endtag
        )
