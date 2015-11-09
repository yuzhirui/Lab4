# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from books.models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author

class BookForm(ModelForm):
    class Meta:
        model = Book
