from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
    template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,template_name='blog/post.html')),

    url(r'^(?P<tags>AMMS)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='AMMS'),template_name='blog/category.html')),
    url(r'^(?P<tags>Windows)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Windows'),template_name='blog/category.html')),
    url(r'^(?P<tags>Drukarki)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Drukarki'),template_name='blog/category.html')),
    url(r'^(?P<tags>Procedury)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Procedury'),template_name='blog/category.html')),
    url(r'^(?P<tags>Finanse)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Ksiegowosc'),template_name='blog/category.html')),
    url(r'^(?P<tags>Pixel)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Pixel'),template_name='blog/category.html')),
    url(r'^(?P<tags>ERP)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='ERP'),template_name='blog/category.html')),
    url(r'^(?P<tags>SEOD)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='SEOD'),template_name='blog/category.html')),
    url(r'^(?P<tags>Backup)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Backup'),template_name='blog/category.html')),
    url(r'^(?P<tags>Tools)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Tools'),template_name='blog/category.html')),
    url(r'^(?P<tags>Wiki)$',ListView.as_view(queryset=Post.objects.filter(tags__icontains='Wiki'),template_name='blog/category.html'))
]
#     (r'^$', 'views.index'),
# url(
#     r'^blog/view/(?P<slug>[^\.]+).html',
#     'views.view_post',
#     name='view_blog_post'),
# url(
#     r'^blog/category/(?P<slug>[^\.]+).html',
#     '.views.view_category',
#     name='view_blog_category'),
# ]
# filter(tags__icontains="AMMS")
