from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:140] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')