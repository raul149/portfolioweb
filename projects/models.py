# Create your models here.
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=450)
    approach = RichTextField(blank=True)
    results = RichTextField(blank=True)
    challen = RichTextField(blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('approach'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('approach', classname="full"),
        FieldPanel('results', classname="full"),
        FieldPanel('challen', classname="full")
    ]
