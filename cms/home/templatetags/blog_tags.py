from django import template

from cms.blog.models import BlogPage

register = template.Library()


@register.assignment_tag(takes_context=False)
def load_latest_blogs(menu_name):
    blogs = BlogPage.objects.live()
    blogs = blogs.order_by('-create_date')

    if blogs:
        if blogs.count() >= 3:
            return blogs[:3]
        else:
            return blogs
    else:
        return None
