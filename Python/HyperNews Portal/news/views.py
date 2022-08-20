from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from random import randint
from .forms import *
import itertools
import json
import os


def read_json_file():
    file_path = os.getcwd()
    with open(f'{file_path}/hypernews/news.json') as f:
        return json.load(f)


def write_post_to_json(form):
    posts = read_json_file()
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    link = randint(100, 1000)
    news_post = {
        'created': created,
        'text': form.cleaned_data['text'],
        'title': form.cleaned_data['title'],
        'link': link
    }
    posts.append(news_post)
    file_path = os.getcwd()
    with open(f'{file_path}/hypernews/news.json', 'w') as f:
        json.dump(posts, f, indent=4)


def sort_news(param=None):
    posts = read_json_file()
    if param:
        lst = []
        for p in posts:
            if param in p['title']:
                lst.append(p)
    else:
        lst = posts

    sorted_news = sorted(lst, key=lambda i: i['created'], reverse=True)
    groupped_news = itertools.groupby(sorted_news, lambda i: i['created'][:10])
    news = {}
    for i, j in groupped_news:
        news[i] = []
        for k in j:
                news[i].append(k)
    return news


def soon(request):
    return redirect('/news/')


def index_view(request):
    form = SearchNews(request.GET)
    if form.is_valid():
        query = form.cleaned_data['q']
        news = sort_news(param=query)
    else:
        news = sort_news()
    return render(request, 'news/index.html', {'news': news, 'form': form})


def create_post(request):
    if request.method == 'POST':
        form = AddNewsPost(request.POST)
        if form.is_valid():
            write_post_to_json(form=form)
            return redirect('/news/')
    else:
        form = AddNewsPost()
    return render(request, 'news/create_post.html', {'form': form})


def show_post(request, post_id):
    post = ''
    for p in read_json_file():
            if p['link'] == int(post_id):
                post = p
    return render(request, 'news/post.html', {'post': post})
