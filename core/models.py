from django.db import models

# Create your models here.
class TimeAudit(models.Model):
    """To path when the data created and modified """
    created=models.DateTimeField(auto_now_add=True,verbose_name="Date Created")
    updated=models.DateTimeField(auto_now=True,verbose_name="Updated")

    class Meta:
        abstract = True

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description=models.TextField(blank=True)
    author=models.CharField(max_length=255)

    def __str__(self):
        return self.title


