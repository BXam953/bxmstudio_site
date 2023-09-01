from django.db import models

class Users(models.Model):
    userName = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    DOA = models.DateField(auto_now_add=True)

class Posts(models.Model):
    postID = models.CharField(max_length=255)
    posted_date = models.DateField(auto_now_add=True)
    contents = models.TextField()

    userName = models.ForeignKey('Users', on_delete=models.CASCADE)


