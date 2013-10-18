from django.db import models

# Create your models here.
class Url(models.Model):
    username = models.CharField(max_length = 20)
    link_url = models.URLField()
    click_num = models.IntegerField()

class TopUrl(models.Model):
    username = models.CharField(max_length = 20)
    top_url = models.URLField()
    num = models.IntegerField()
