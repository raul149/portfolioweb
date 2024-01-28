
# Create your views here.
from django.shortcuts import render
from wagtail.models import Page

def blog_page(request, slug):
    # Find the Wagtail page with the given slug
    page = Page.objects.get(slug=slug)

    # Render the page template
    return render(request, 'blog/blog_page.html', {'page': page})