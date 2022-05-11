from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Title')
    position = models.IntegerField(default=0, blank=False, null=False, verbose_name='Index position')


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Title')
    post_text = models.TextField(verbose_name='Text')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Add time')