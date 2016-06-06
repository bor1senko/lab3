from django.db.models.signals import post_save

from django.db import models
import requests
from lxml import html
import My_functions
import re
level_recursian = 3
y = []

class URLL(models.Model):
    index = models.TextField(editable=False)
    url_adres = models.URLField(max_length = 200)
    second_index = models.TextField(editable=False)
    pos = models.IntegerField(editable=False,null=True )

    def save(self):
        if self.pos == None:
            self.pos = 0
        page = requests.get(self.url_adres)
        p = html.fromstring(page.content)
        l = []
        l.extend(p.xpath('//p/text()'))
        l.extend(p.xpath('//li/text()'))
        l.extend(p.xpath('//span/text()'))
        l.extend(p.xpath('//a/text()'))
        l.extend(p.xpath('//h1/text()'))
        l.extend(p.xpath('//h2/text()'))
        l.extend(p.xpath('//h3/text()'))
        r = []
        for item in p.xpath("//a"):
            temper  = item.get("href")
            if self.pos == 0:
                if My_functions.proov(temper) == True:
                    r.append(str( temper))
        #print r
        self.second_index = ' '.join(r)
        self.index = ' '.join(l)
        super(URLL, self).save()

    def reborn (self):
        self.pos = 1


    def __str__(self):
        return str(self.url_adres)


class Text(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text.split(' ')[0].encode('utf8')


def my_save(sender, instance, **kwargs):
    print instance
    print "Save finished!"
    print sender
    from models import URLL
    c = "<class 'firstapp.models.URLL'>"
    print c
    if str(sender) == "<class 'firstapp.models.URLL'>":
        if instance.pos == 0:
            tmp = instance.second_index.split(" ")
            if type(tmp) == list and len(tmp)>1:
                instance.reborn()
                for k in tmp:
                    if k not in URLL.objects.all():
                        print "ADDED " ,k ,"  in URLLS"
                        URLL(url_adres=k, pos=1).save()

post_save.connect(my_save)


#from models import URLL



class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

book = Book.objects.create_book("Pride and Prejudice")
