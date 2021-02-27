from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import Post


def home(request):
    queryset = Post.objects.all()

    paginator = Paginator(queryset, 4)
    page_request_variable = 'page'
    page = request.GET.get(page_request_variable)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'posts': paginated_queryset,
        'page_request_variable': page_request_variable,
    }
    return render(request, 'blog/index.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)
