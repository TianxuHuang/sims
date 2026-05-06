from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='课程名称')
    credits = models.IntegerField(verbose_name='学分')
    hours = models.IntegerField(verbose_name='课时')
    description = models.TextField(blank=True, null=True, verbose_name='课程描述')

    class Meta:
        db_table = 'courses'
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name
