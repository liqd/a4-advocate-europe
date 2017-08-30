from django import forms
from wagtail.wagtailcore.blocks import (CharBlock, ChoiceBlock, ChooserBlock,
                                        ListBlock, PageChooserBlock,
                                        RichTextBlock, StreamBlock,
                                        StructBlock, TextBlock, URLBlock)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from adhocracy4.projects.models import Project
from apps.ideas import filters
from apps.ideas.models.abstracts import idea_section


class LinkBlock(StructBlock):
    link = URLBlock(required=True)
    link_text = CharBlock(required=True)


class TeasertextBlock(StructBlock):
    headline = CharBlock(required=True, length=256)
    text = TextBlock(required=True)
    link = PageChooserBlock(required=False)
    link_text = CharBlock(required=False,
                          help_text=("Text to be displayed on the link-button."
                                     "Should be quite short! If not given, the"
                                     "title of the linked page will be used.")
                          )

    class Meta:
        template = 'cms_home/blocks/teasertext_block.html'


class ThreeColumnTextBlock(StructBlock):
    title = CharBlock(required=False, length=256)

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


class ProjectChooserBlock(ChooserBlock):
    target_model = Project
    widget = forms.widgets.Select


class ProposalCarouselBlock(StructBlock):
    headline = CharBlock(required=False)
    year = ProjectChooserBlock(required=False)
    topic = ChoiceBlock(choices=idea_section.IDEA_TOPIC_CHOICES,
                        required=False)
    ordering = ChoiceBlock(choices=filters.ORDERING_CHOICES, required=False)
    status = ChoiceBlock(choices=filters.STATUS_FILTER_CHOICES, required=False)

    class Meta:
        template = 'cms_home/blocks/carousel_block.html'
        icon = 'folder-inverse'
        label = 'Carousel Block'
        help_text = 'Displays up to 20 ideas that match the filters'


class QuestionAnswerBlock(StructBlock):
    question = CharBlock()
    answer = RichTextBlock()

    class Meta:
        template = 'cms_home/blocks/question_answer_block.html'


class FAQBlock(StructBlock):
    title = CharBlock(required=False)
    faqs = ListBlock(QuestionAnswerBlock)

    class Meta:
        template = 'cms_home/blocks/faq_block.html'


class SectionBlock(StructBlock):
    title = CharBlock(label="Section Title")
    content = StreamBlock(
        [
            ('text', RichTextBlock(required=False)),
            ('FAQ', FAQBlock(required=False))
        ]
    )


class ThreeBlogEntriesBlock(StructBlock):
    title = CharBlock(required=False,
                      help_text="Heading to show above the blog entries"
                      )
    link = PageChooserBlock(required=False, help_text="Link to blog overview")

    class Meta:
        template = 'cms_home/blocks/blog_block.html'
        label = 'Latest Blog Post'
        help_text = 'The three latest blog entries'


class ImageWithLinkBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    link = URLBlock(required=False)

    class Meta:
        template = 'cms_home/blocks/image_with_link.html'


class ThreeImagesBlock(StructBlock):
    image_left = ImageWithLinkBlock(required=False)
    image_middle = ImageWithLinkBlock(required=False)
    image_right = ImageWithLinkBlock(required=False)

    class Meta:
        template = 'cms_home/blocks/three_images_block.html'
        label = 'Three images block'
        help_text = 'Three images in a row'
