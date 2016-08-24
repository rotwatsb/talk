from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField
    block_hash = models.CharField
    
