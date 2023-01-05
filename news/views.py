from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Post


def index(request):
    return render(request, 'news/index.html', context={
        'page_title': _('PageTitle'),
        'all_news': Post.objects.all()
    })
