from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, ObjectList,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):

    subpage_types = ['cms_blog.BlogPage']

    @property
    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by('-create_date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs
        page = request.GET.get('page')
        paginator = Paginator(blogs, 5)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context


class BlogPage(Page):

    title_blog = models.CharField(
        max_length=255, blank=True, verbose_name="Blog Title")
    teasertext = models.TextField(
        blank=True, null=True, verbose_name="Blog Teaser Text")
    author = models.CharField(
        max_length=255, blank=True, verbose_name="Author Name")
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    body = RichTextField(blank=True, verbose_name="Blog Text")
    categories = ParentalManyToManyField('cms_snippets.Category', blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Blog Image",
        help_text="The Image that is shown on the blog page " +
        "and in the blog index page"
    )

    subpage_types = []

    content_panels = [
        FieldPanel('title_blog'),
        FieldPanel('teasertext'),
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ImageChooserPanel('image'),
    ]

    promote_panels = Page.content_panels + Page.promote_panels

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote')
    ])
