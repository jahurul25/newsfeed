from django.db import models

# Create your models here.

class NewsInfo(models.Model): 
    source_name        = models.CharField(max_length=150, verbose_name="Source Name") 
    author             = models.CharField(max_length=150, verbose_name="Author", blank=True, null=True) 
    haeadline          = models.TextField(blank=True, null=True)
    news_source        = models.TextField(blank=True, null=True)
    content            = models.TextField(blank=True, null=True)
    thumbnail          = models.TextField(blank=True, null=True)
    country_of_news    = models.CharField(max_length=50, verbose_name="Country of News", blank=True, null=True) 
    published_at       = models.DateTimeField(auto_created=False)
    deleted            = models.BooleanField(default=False)

    def __str__(self):
        return str(self.haeadline)

    class Meta:
        managed   = True
        ordering  = ["-published_at"]
        db_table  = "news_info"
        verbose_name_plural = "News Info"

class NewsfeedSettings(models.Model): 
    country        = models.TextField(blank=True, null=True)
    news_source    = models.TextField(blank=True, null=True) 
    news_keyword   = models.TextField(blank=True, null=True)
    deleted        = models.BooleanField(default=False)

    def __str__(self):
        return str(self.country)

    class Meta:
        managed   = True
        ordering  = ["-id"]
        db_table  = "newsfeed_settings"
        verbose_name_plural = "News Settings "