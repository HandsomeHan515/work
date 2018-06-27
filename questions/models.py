from django.db import models
from ablitys.models import Ablity


class Question(models.Model):
    level_choices = (('1', '一级'),
                     ('2', '二级'),
                     ('3', '三级'))

    name = models.CharField(max_length=512)
    ablity = models.ForeignKey(Ablity, related_name='ablitys')
    level = models.CharField(max_length=16, choices=level_choices)
    analysis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
