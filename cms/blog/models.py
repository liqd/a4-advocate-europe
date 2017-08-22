from django import forms
from django.core.paginator import InvalidPage, Paginator
from django.db import models
from django.http import Http404
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, PageChooserPanel,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from cms.snippets.models import Category


class BlogIndexPage(Page):

    featured_page = models.ForeignKey(
        'cms_blog.BlogPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    subpage_types = ['cms_blog.BlogPage']

    @property
    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by('-create_date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs

        category = request.GET.get('category')
        if category:
            blogs = blogs.filter(categories__pk=category)

        page = request.GET.get('page', 1)
        paginator = Paginator(blogs, 5)

        try:
            blogs = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        context['categories'] = Category.objects.all()
        context['category'] = category
        return context

    content_panels = [
        FieldPanel('title'),
        PageChooserPanel('featured_page'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('search_description')
        ])
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote')
    ])


class BlogPage(Page):

    teasertext = models.TextField(
        blank=True, null=True, verbose_name="Blog Teaser Text")
    author = models.CharField(
        max_length=255, blank=True, verbose_name="Author Name")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
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
        "and the blog index page"
    )

    subpage_types = []

    content_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('teasertext'),
            FieldPanel('author'),
            FieldPanel('body', classname="full"),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ImageChooserPanel('image')
        ]),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('search_description')
        ])
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote')
    ])

    @property
    def creator(self):
        return self.owner
