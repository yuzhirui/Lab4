# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from books.models import Book, Author
from books.forms import AuthorForm, BookForm

def home(request):
    books = Book.objects.all()
    if 's' in request.GET:
        isbn = request.GET['s']
        get_object_or_404(Book, ISBN = isbn).delete()
    return render_to_response('index.html',
                              {'books': books})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append(u'请输入搜索字段')
        elif len(q) > 30:
            errors.append(u'最多输入不超过30个字')
        else:
            books = Book.objects.filter(Authors__Name__icontains = q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})

def detail(request):
    isbn = request.GET['q']
    thebook = get_object_or_404(Book, ISBN = isbn)
    authors = thebook.Authors.all()
    return render_to_response('detail.html',
            {'book': thebook, 'authors': authors})

def change(request):
    isbn = request.GET['q']
    thebook = get_object_or_404(Book, ISBN = isbn)
    if request.POST:
        newbook = BookForm(request.POST, instance = thebook)
        if newbook.is_valid():
            newbook.save()
            return render_to_response('change.html',
                    {
                        'newbook': newbook,
                        'msg': u'图书修改成功！',
                    })
        else:
            newbook = BookForm(instance = thebook)
            return render_to_response('change.html', {'newbook': newbook,})
    else:
        newbook = BookForm(instance = thebook)
        return render_to_response('change.html', {'newbook': newbook,})

def delbook(request):
    isbn = request.GET['q']
    thebook = get_object_or_404(Book, ISBN = isbn)
    authors = thebook.Authors.all()
    return render_to_response('delete.html', {'book': thebook, 'authors': authors})

def newbook(request):
    abook = None

    if request.POST:
        book = Book()
        abook = BookForm(request.POST, instance = book)

        if abook.is_valid():
            abook.save()
            return render_to_response('newbook.html',
                    {
                        'abook': abook,
                        'msg': u'图书添加成功！',
                    })
        else:
            abook = BookForm()
            return render_to_response('newbook.html', {'abook': abook, 'msg': u'图书添加失败，请检查信息是否正确'})
    else:
        abook = BookForm()
        return render_to_response('newbook.html', {'abook': abook,})
def newauthor(request):
    if request.POST:
        author = Author()
        aauthor = AuthorForm(request.POST, instance = author)
        
        if aauthor.is_valid():
            aauthor.save()
            return render_to_response('newauthor.html',
                    {
                        'aauthor': aauthor,
                        'msg': u'作者添加成功',
                    })
        else:
            aauthor = AuthorForm()
            return render_to_response('newauthor.html', {'aauthor': aauthor,'msg': u'作者添加失败，请检查信息是否正确'})
    else:
        aauthor = AuthorForm()
        return render_to_response('newauthor.html', {'aauthor': aauthor,})
