from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name='班级名称')

    class Meta:
        db_table = 'classes'
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.name
