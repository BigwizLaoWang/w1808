# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="name"
    )
    IssueDate=models.DateField(
        auto_now=True,
        verbose_name="发行时间"
    )
    modtime=models.DateTimeField(
        auto_now_add=True,
        verbose_name="修改时间"
    )
    price=models.IntegerField(
        default=5000,
        verbose_name="价格"
    )

    class Meta:
        verbose_name="电影"
        db_table="movie theater"