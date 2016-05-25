from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class URLL(models.Model):
    url_adres = models.URLField(max_length = 200)
    add_name =  models.ForeignKey(Author)
    def __str__(self):
        return str(self.add_name) + '_add_' + str(self.url_adres)

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
    #@permalink
    def get_absolute_url(self):
        return ('item_detail', None,{'object_id': self.id})


class Photo(models.Model):
    item = models.ForeignKey(Item)
    add_name = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='photos')

    class Meta:
        ordering =['title']

    def __unicode__(self):
        return self.title

#    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None,{'object_id': self.id})
