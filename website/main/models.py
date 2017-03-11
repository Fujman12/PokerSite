from django.db import models
from django.contrib import auth
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 250)
    summary = models.CharField(blank = True, max_length = 350)
    content = models.TextField()
    published = models.BooleanField(default = False)
    active = models.BooleanField(default = False)

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    img_url = models.CharField(max_length = 500, default = 'http://www.poker.no/wp-content/uploads/2017/02/Karl-Fredrik-R%C3%B8sok-620x330.jpg')

    category = models.ForeignKey('Category', blank = True)
    author = models.ForeignKey('auth.User', default = 1)

    def __str__(self):
        return self.title + "-" + self.summary + " // " + self.author.username

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

### Temporary, will be changed later
"""
class User(models.Model):
    username = models.CharField(max_length = 30)

    def __str__(self):
        return self.username
"""
