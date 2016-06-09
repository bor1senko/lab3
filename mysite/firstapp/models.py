from django.db import models
import requests
import parser
from lxml import html
from django.dispatch import receiver
from django.db.models.signals import post_save



class URLL(models.Model):
    url_adres = models.URLField(max_length=200)
    index = models.TextField(editable=False)
    title = models.CharField(max_length=200, editable=False)
    flag = models.BooleanField(editable=False, default=False)
    hight_recurcian = models.IntegerField(default = 0)
    i = int()
    def save(self):
        if self.hight_recurcian == 0:
            self.flag = True
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
        try:
            self.title = p.xpath('//title/text()')[0]
        except IndexError:
            self.title = self.url_adres.split("/")[2]
        super(URLL, self).save()

    def __str__(self):
        return str(self.url_adres)

@receiver(post_save, sender=URLL)
def dfs_url(instance, **kwargs):
    print instance.url_adres
    if instance.flag == False:
        page = requests.get(instance)
        page = html.fromstring(page.content)
        l = page.xpath('//a/@href')[:100]
        l = set(l)
        for url in l :
            if url.startswith("http") or url.startswith("https"):
                URLL(url_adres=url, flag=True ,hight_recurcian=instance.hight_recurcian-1).save()


class Text(models.Model):
    text = models.TextField()
    flag = models.BooleanField(editable=False,default=False)
    def __str__(self):
        return self.text.split(' ')[0].encode('utf8')
    def save(self, *args, **kwargs):
        super(Text, self).save(*args, **kwargs)
