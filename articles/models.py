from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def lbody(self):
        return self.body[:50] + ' ...'