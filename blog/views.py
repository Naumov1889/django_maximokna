from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.utils import get_page_range
from .models import Post

def blog(request):
    posts = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(posts, 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    index = posts.number - 1
    max_index = len(paginator.page_range)

    start_index, end_index = get_page_range(index, max_index)
    page_range = list(paginator.page_range)[start_index:end_index]

    ###
    pagination_html = ''
    if posts.paginator.num_pages > 1:
        pagination_html = '<div class="pagination pagination_has-padding_top">'

        if posts.number > 1:
            if posts.number - 1 == 1:
                pagination_html += '<a class="pagination__prev" ' \
                                   'href="' + request.path + '"><i class="icon icon_arrow_type-2"></i></a>'
            else:
                pagination_html += '<a class="pagination__prev" ' \
                                   'href="' + request.path + '?page=' + str(
                    posts.number - 1) + '"><i class="icon icon_arrow_type-2"></i></a>'

        if start_index > 0:
            pagination_html += '<a class="pagination__first" ' \
                               'href="' + request.path + '">Первая</a>'

        pagination_html += '<div class="pagination__list">'

        for i in page_range:
            if posts.number == i:
                pagination_html += '<a class="pagination__item pagination__item_active" ' \
                                   'href="#">' + str(i) + '</a>'
            elif i == 1:
                pagination_html += '<a class="pagination__item" ' \
                                   'href="' + request.path + '">1</a>'
            else:
                pagination_html += '<a class="pagination__item" ' \
                                   'href="' + request.path + '?page=' + str(i) + '">' + str(i) + '</a>'

        pagination_html += '</div>'

        if end_index < posts.paginator.num_pages:
            pagination_html += '<a class="pagination__last" ' \
                               'href="' + request.path + '?page=' + str(posts.paginator.num_pages) + '">Последняя</a>'
        if posts.number != posts.paginator.num_pages:
            pagination_html += '<a class="pagination__next" ' \
                               'href="' + request.path + '?page=' + str(posts.number + 1) + '">' \
                                                                                             '<i class="icon icon_arrow_type-2"></i></a>'

        pagination_html += '</div>'
    
    
    context = {
        "posts": posts,
        'pagination_html': pagination_html,
        "black_burger": True
    }
    return render(request, "blog/blog.html", context)


def post(request, slug):
    context = {
        "article": get_object_or_404(Post, slug=slug),
        "black_burger": True
    }
    return render(request, "blog/blog-inner.html", context)
