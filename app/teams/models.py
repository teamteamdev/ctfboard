from django.db import models


class Team(models.Model):
    competition = models.CharField(max_length=40)
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    score = models.PositiveIntegerField(default=0)
    last_submit = models.DateTimeField(default=None, null=True, blank=True)
    
    @property
    def place(self):
        if self.score == 0:
            return "∞"
        return Team.objects.filter(score__gt=self.score, competition=self.competition).count() + Team.objects.filter(score=self.score, competition=self.competition, last_submit__lt=self.last_submit).count() + 1

    def __str__(self): return self.name