from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"<Book Object: {self.id} {self.title} {self.desc}>"

class Author(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  books = models.ManyToManyField(Book, related_name="authors")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"<Author Object: {self.id} {self.first_name} {self.last_name}>"