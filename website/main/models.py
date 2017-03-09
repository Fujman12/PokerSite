from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 250)
    summary = models.CharField(blank = True, max_length = 350)
    content = models.TextField()
    published = models.BooleanField(default = False)
    active = models.BooleanField(default = False)

    date_created = models.DateTimeField()

    img_url = models.CharField(max_length = 500)

    category = models.ForeignKey('Category', blank = True)
    author = models.ForeignKey('User', default = 1)

    def __str__(self):
        return self.title + "-" + self.summary + " // " + self.author.username

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

### Temporary, will be changed later
class User(models.Model):
    username = models.CharField(max_length = 30)

    def __str__(self):
        return self.username
