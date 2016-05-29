from django.shortcuts import render
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import URLL,Text
from django.shortcuts import render_to_response
from django.db.models.query import QuerySet

def index(request):
        url_list = URLL.objects.all()
        template = loader.get_template('firstapp/index.html')
        context = RequestContext(request, {'url_list': url_list,})
        return HttpResponse(template.render(context))


def index2(request):
    listic = Text.objects.all()
    template = loader.get_template('firstapp/index2.html')
    context = RequestContext(request, {'listic':listic,})
    return HttpResponse(template.render(context))

def search_form(request):
    return render_to_response('firstapp/search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        listic = Text.objects.filter(text__icontains=q)
        template = loader.get_template('firstapp/index2.html')
        context = RequestContext(request, {'listic': listic,})
    return HttpResponse(template.render(context))
