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
    name = models.CharField(max_length=128)
    level_two = models.ForeignKey(AblityLevelTwo, null=True)
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    is_level = models.BooleanField(default=False)
    content = models.TextField(blank=True, null=True)
    one = models.TextField(blank=True, null=True)
    two = models.TextField(blank=True, null=True)
    three = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def level_one(self):
        return self.level_two.parent.id
