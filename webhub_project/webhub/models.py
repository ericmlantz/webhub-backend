from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Interest(models.Model):
  topic = models.CharField(max_length=100)
  description = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'interests')

  def __str__(self):
    return self.topic

class Search(models.Model):
  query = models.CharField(max_length = 100)
  results = ArrayField(models.JSONField(), blank=True)
  interest = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name = 'searches')
  
  def __str__(self):
    return self.query

class Page(models.Model):
  title = models.CharField(max_length = 100)
  url = models.TextField()
  interest = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name = 'pages')

  def __str__(self):
    return self.title

class Note(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name = 'notes')
  
  def __str__(self):
    return self.title
