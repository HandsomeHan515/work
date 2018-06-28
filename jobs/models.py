from django.db import models


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
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
