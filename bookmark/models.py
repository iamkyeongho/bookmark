from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length = 200)
    url = models.URLField("Site URL")    

    def __str__(self,):
        return "사이트명 : {site_name}, 사이트주소 : {site_url}".format(site_name=self.site_name, site_url=self.url)       

    def get_absolute_url(self,):
        return reverse("bookmark:detail", args=[str(self.id)]) 

