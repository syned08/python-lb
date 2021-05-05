from django.shortcuts import render, redirect
from django.db.models import F
# from django.http import HttpResponse

from .models import Links


def index(request):
    links = Links.objects.order_by('-created_at')
    context = {
        'title': 'Ссылки',
        'links': links
    }
    return render(request, 'links/index.html', context)


def go_link(request, post_id):
    link = Links.objects.get(pk=post_id)
    link.count_visites = F('count_visites') + 1
    link.save()
    return redirect(link.link_name)
