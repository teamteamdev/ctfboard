from django.db import models


class Submit(models.Model):
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE)
    task = models.SlugField(max_length=30)
    text = models.CharField(max_length=60)
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Hint(models.Model):
    pass