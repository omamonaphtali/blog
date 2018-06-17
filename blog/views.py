# from urllib import quote

from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def index_view(request):
    context = {
        "title": "Home"
    }
    return render(request, 'post_list.html', context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "New Post",
        "form": form
    }
    return render(request, 'post_form.html', context)


def post_detail(request, pk):
    instance = get_object_or_404(Post, id=pk)
    # share_string = quote(instance.content)
    context = {
        "title": "Detail",
        "post": instance,
        # "share_string": share_string
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")
    # search query
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 4)  # Show 4 items per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "title": "List",
        "object_list": queryset,
        "page_request_var": page_request_var
    }
    return render(request, 'post_list.html', context)


def post_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully updated")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "post": instance,
        "form": form,
        "title": "Update"
    }
    return render(request, 'post_form.html', context)


def post_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=pk)
    instance.delete()
    # context = {
    #     "title": "Delete Post"
    # }
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")
