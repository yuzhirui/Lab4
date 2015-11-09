# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=80, verbose_name = u'作者姓名')
    Age = models.IntegerField(max_length=3, blank=True, null=True, verbose_name = u'年龄')
    Country = models.CharField(max_length=40, blank=True, null=True, verbose_name = u'国籍')

    def __unicode__(self):
        return u'%s' % (self.Name)

class Book(models.Model):
    ISBN = models.CharField(max_length=30, primary_key = True)
    Title = models.CharField(max_length=100, verbose_name = u'书名')
    Authors = models.ManyToManyField(Author, verbose_name = u'作者')
    Publisher = models.CharField(max_length=40, verbose_name = u'出版社')
    PublishDate = models.DateField(blank=True, null=True, verbose_name = u'出版日期')
    Price = models.FloatField(max_length=20, blank=True, null=True, verbose_name = u'价格')

    def __unicode__(self):
        return self.Title
