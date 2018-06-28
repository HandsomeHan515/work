from django.db import models
from ablitys.models import Ablity


class Question(models.Model):
    name = models.CharField(max_length=512)
    ablity = models.ForeignKey(Ablity, related_name='questions')
    analysis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def ablity_level(self):
        return self.ablity.level
