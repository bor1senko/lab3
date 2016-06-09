from celery import task
from .models import URLL

import requests
from requests import RequestException


@task.task
def first(l, recursion_value):
    for url in l :
        prime = False

        for i in URLL.objects.all():
            if str(i)==str(url):
                prime = True
        try:
            x = requests.get(url)
            x.raise_for_status()
            print "++"
        except (requests.exceptions.HTTPError, RequestException):
            prime = True
            print url
            print "--"
        if prime==False  and (url.startswith("http") or url.startswith("https")):
            print url + " +++ "
            URLL(url_adres=u'%s'%url,hight_recurcian=recursion_value-1).save()
