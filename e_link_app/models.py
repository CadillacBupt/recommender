from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(unique=True,max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField(unique=True)

class Tag(models.Model):
    username = models.CharField(max_length = 20)
    tag_name = models.CharField(max_length = 20)
  
class Field(models.Model):
    username = models.CharField(max_length = 20)
    field_name = models.CharField(max_length = 20)
    parent_name = models.CharField(max_length = 20) 


class Link(models.Model):
    link_url= models.URLField()
    username = models.CharField(max_length = 20)
    link_name = models.CharField(max_length = 20)
    link_tag = models.CharField(max_length = 20)
    link_field = models.CharField(max_length = 20)
    like_num = models.IntegerField()
    dislike_num = models.IntegerField()
    used_num = models.IntegerField()

