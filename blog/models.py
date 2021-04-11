from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.shortcuts import reverse

CHOICES = [
    ("aboutus", 'About us'),
    ("contactus", 'Contact us'),
]


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50,choices=CHOICES)
    text = RichTextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    image= models.ImageField(upload_to="category/images/%Y/%m/%d")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categorydetail', kwargs={'slug':self.slug})

    def show_image(self):
        return format_html("<img style='width:150;height:150' src='{}' alt='post image'>".format(self.image.url))

class SubCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    name   = models.CharField(max_length=20)
    slug   = models.SlugField(max_length=20)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategorydetail', kwargs={'slug':self.slug})

    def show_parent(self):
        return self.parent.name


class Post(models.Model):
    name        = models.CharField(max_length=20)
    slug        = models.SlugField(max_length=20)
    image       = models.ImageField(upload_to="posts/images/%Y/%m/%d")
    text        = RichTextField()
    category    = models.ManyToManyField("Category")
    subcategory = models.ManyToManyField("SubCategory")
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})
    
    def show_image(self):
        return format_html("<img style='width:150;height:150' src='{}' alt='post image'>".format(self.image.url))

    show_image.short_description = "Images"
    show_image.allow_tags = True

    def show_category(self):
        return ", ".join([x.name for x in self.category.all()])

    def show_subcategory(self):
        return ", ".join([x.name for x in self.subcategory.all()])

    def show_author(self):
        return self.author.username
