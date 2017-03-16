from wagtail.wagtailcore.blocks import (CharBlock, PageChooserBlock,
                                        StructBlock, TextBlock,
                                        URLBlock)


class LinkBlock(StructBlock):
    link = URLBlock(required=True)
    link_text = CharBlock(required=True)


class TeasertextBlock(StructBlock):

    headline = CharBlock(required=True, length=256)
    text = TextBlock(required=True)
    link = PageChooserBlock(required=False)

    class Meta:
        template = 'cms_home/blocks/teasertext_block.html'


class ThreeColumnTextBlock(StructBlock):

    title = CharBlock(required=True, length=256)

    col1 = TeasertextBlock(required=True)
    col2 = TeasertextBlock(required=True)
    col3 = TeasertextBlock(required=True)

    class Meta:
        template = 'cms_home/blocks/three_column_text_block.html'
        icon = 'grip'
        label = '3 Column Text'
        help_text = 'Text in 3 columns with optional column heading and link.'


class CallToActionBlock(StructBlock):

    headline = CharBlock(required=True)
    link = LinkBlock(required=True)
    text = TextBlock(required=True)

    class Meta:
        template = 'cms_home/blocks/call_to_action_block.html'
        icon = 'pick'
        label = 'Call to Action'
        help_text = 'Call to action with button and text'
