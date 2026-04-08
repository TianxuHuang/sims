from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, verbose_name='学号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    birthday = models.DateField(verbose_name='生日')
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='性别')
    phone = models.CharField(max_length=20, verbose_name='电话')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=200, verbose_name='家庭地址')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='头像', blank=True, null=True)
    
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
    
    def __str__(self):
        return f'{self.student_id} - {self.name}'
