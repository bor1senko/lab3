from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class URLL(models.Model):
    url_adres = models.URLField(max_length = 200)
    add_name =  models.ForeignKey(Author)
    def __str__(self):
        return str(self.add_name) + '_add_' + self.url_adres
