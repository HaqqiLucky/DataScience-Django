from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class Link(models.Model) :
    judul = models.CharField(max_length=100)
    tgl_dibuat = models.DateField()
    tgl_dipublish = models.DateField(auto_now_add=True)
    konten = MarkdownxField()
    slug = models.SlugField()

    def get_konten_html(self):
        return markdownify(self.konten)
    
    def __str__(self):
        return self.judul