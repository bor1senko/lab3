from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import URLL

def index(request):
        url_list = URLL.objects.order_by('add_name')[:3]
        template = loader.get_template('firstapp/index.html')
        context = RequestContext(request, {'url_list': url_list,})
        return HttpResponse(template.render(context))

def detail(request,add_name_id):
    return HttpResponse("kokokookokokokokok o %s" % add_name_id)
