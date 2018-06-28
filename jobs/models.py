from django.db import models
from ablitys.models import Ablity


class JobLevelOne(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class JobLevelTwo(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        JobLevelOne, related_name='level_twos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=128)
    level_two = models.ForeignKey(JobLevelTwo, related_name='jobs')
    ablitys = models.ManyToManyField(
        Ablity, related_name='job_ablitys', through='JobAblityShip')
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def level_one(self):
        return self.level_two.parent.name

    @property
    def ablity(self):
        return self.ablitys.count()

    @property
    def question(self):
        num = 0
        for item in self.ablitys.all():
            num = num + item.questions.count()
        return num


class JobAblityShip(models.Model):
    job = models.ForeignKey(Job)
    ablity = models.ForeignKey(Ablity, related_name='nums')
    num = models.PositiveIntegerField()

    class Meta:
        ordering = ('num',)
