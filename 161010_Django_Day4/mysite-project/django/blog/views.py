from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.db.models import Q
from .models import Post

# 같은 의미
# from blog.models import Post


def post_list(request):
    # posts = Post.objects\
    #     # .filter(published_date__lte=timezone.now())\
    #     .order_by('published_date')

    posts = Post.objects \
        .filter(published_date__lte=timezone.now())\
    .order_by('published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts, 'title': '타이틀 변수는 title키를 이용해서 접근'})
