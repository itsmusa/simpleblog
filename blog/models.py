from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save

from ckeditor_uploader.fields import RichTextUploadingField
from simpleblog.utils import unique_slug_generator

class Post(models.Model):

    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', default='default.jpg')
    description = models.CharField(max_length=150)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pub_date',)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)
