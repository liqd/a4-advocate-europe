from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, ObjectList,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from cms.snippets.models import Category


class BlogIndexPage(Page):

    title_blog_index = models.CharField(
        max_length=255, blank=True, verbose_name="Blog Index Title")

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
            blogs = blogs.filter(categories__name_en=category)

        page = request.GET.get('page')
        paginator = Paginator(blogs, 5)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Only show five page numbers in pagination
        index = blogs.number - 1
        max_index = len(paginator.page_range)
        if index <= 1:
            start_index = 0
            end_index = 4
        elif index >= max_index - 2:
            start_index = max_index - 5 if max_index > 5 else 0
            end_index = max_index
        else:
            start_index = index - 2
            end_index = index + 2
        page_range = paginator.page_range[start_index:end_index+1]

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        context['categories'] = Category.objects.all()
        context['category'] = category
        context['page_range'] = page_range
        return context

    content_panels = [
        FieldPanel('title_blog_index'),
    ]

    promote_panels = Page.content_panels + Page.promote_panels

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote')
    ])


class BlogPage(Page):

    title_blog = models.CharField(
        max_length=255, blank=True, verbose_name="Blog Title")
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
