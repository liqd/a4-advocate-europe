from wagtail.wagtailcore.blocks import CharBlock, PageChooserBlock, StructBlock


class LinkBlock(StructBlock):
    link = PageChooserBlock(required=True)
    link_text_en = CharBlock(required=True)
    link_text_de = CharBlock(required=False)
