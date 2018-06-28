from django.db import models


class AblityLevelOne(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class AblityLevelTwo(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        AblityLevelOne, related_name='ablity_level_ones')

    def __str__(self):
        return self.name


class Ablity(models.Model):
    level_choices = (('1', '一级'),
                     ('2', '二级'),
                     ('3', '三级'))

    name = models.CharField(max_length=128)
    level_two = models.ForeignKey(AblityLevelTwo, null=True)
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    level = models.CharField(
        max_length=16, choices=level_choices, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    one = models.TextField(blank=True, null=True)
    two = models.TextField(blank=True, null=True)
    three = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def level_one(self):
        return self.level_two.parent.id

    @property
    def question(self):
        return self.questions.count()

    @property
    def job(self):
        return self.job_ablitys.count()
