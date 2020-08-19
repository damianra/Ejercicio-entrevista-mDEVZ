from django.db import models


class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    search_text = models.CharField(max_length=150)
    date = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'search_history'


class Tweet(models.Model):
    user = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    text = models.CharField(max_length=200)
    created = models.CharField(max_length=200)
    id_tw = models.IntegerField()
