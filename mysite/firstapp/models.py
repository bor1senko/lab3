from django.db import models
import requests
import parser
from lxml import html



class URLL(models.Model):
    url_adres = models.URLField(max_length = 200)
    index = models.TextField(editable=False)
    def save(self):
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
        self.index = ' '.join(l)
        super(URLL, self).save()
    def __str__(self):
        return str(self.url_adres)





class Text(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text.split(' ')[0].encode('utf8')
