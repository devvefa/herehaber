from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    Status = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=110)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.ImageField(blank=True, upload_to='image/', null=True)
    status = models.CharField(max_length=30, choices=Status)
    slug = models.SlugField(null=False,unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='chidren', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])


class News(models.Model):
    Status = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    # ------------1(cat) to many(news)----------

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=110, blank=True, )
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='image/', null=True)
    detail = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=30, choices=Status)
    tags = models.CharField(max_length=255, blank=True)
    read_time = models.IntegerField(default=0, blank=True)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=False,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Imgs(models.Model):
    # ------------1(news) to many(images)----------
    haber = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=110, blank=True)
    image = models.ImageField(blank=True, upload_to='image/', null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    Status = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    # ------------1(cat) to many(news)----------
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    rate = models.PositiveIntegerField(default=0)

    note = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=Status,default='New')
    ip = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'subject', 'comment','note']
        widgets = {
            'note': TextInput(attrs={'class': 'input', 'placeholder': 'note'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Konu'}),
            'comment': TextInput(attrs={'class': 'input', 'placeholder': 'yourum'}),
        }