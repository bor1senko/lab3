from django.db import models
import requests
import parser
from lxml import html

depth = 3


class URLL(models.Model):
    url_adres = models.URLField(max_length=200)
    index = models.TextField(editable=False)
    title = models.CharField(max_length=200, editable=False)
    def dfs(self, url, h):
        if h == 0:
            page = requests.get(url)
            p = html.fromstring(page.content)
            l = []
            l.extend(p.xpath('//p/text()'))
            l.extend(p.xpath('//li/text()'))
            l.extend(p.xpath('//span/text()'))
            l.extend(p.xpath('//a/text()'))
            l.extend(p.xpath('//h1/text()'))
            l.extend(p.xpath('//h2/text()'))
            l.extend(p.xpath('//h3/text()'))
            self.index = ' '.join(l)
            self.title = p.xpath('//title/text()')[0]

    def save(self):
        self.dfs(self.url_adres, 0)
        super(URLL, self).save()

    def __str__(self):
        return str(self.url_adres)


class ttt(models.Model):
    text = models.TextField()
    def ko(self):
        self.text = "213"


class Text(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text.split(' ')[0].encode('utf8')
