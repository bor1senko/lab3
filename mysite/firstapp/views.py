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
    listic = URLL.objects.all()
    template = loader.get_template('firstapp/index2.html')
    context = RequestContext(request, {'listic':listic,})
    return HttpResponse(template.render(context))

def search_form(request):
    return render_to_response('firstapp/search_form.html')

def search(request):
    q =str()
    if 'q' in request.GET:
        q = request.GET['q']
    listic = set()
    q = q.split(' ')
    for qq in q:
        if qq != '':
            listic = listic.union(list(URLL.objects.filter(index__icontains=qq.lower())))
    q = " ".join(q)
    if len(listic) == 0 and q == '':
        listic = URLL.objects.all()
    template = loader.get_template('firstapp/index2.html')
    context = RequestContext(request, {'listic': listic, 'q': q, })
    return HttpResponse(template.render(context))
