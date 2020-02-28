from django.db import models

# Create your models here.




class Province(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True, verbose_name='省份')

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = "省份"



    def __str__(self):
        return self.name

class User(models.Model):
    user_level = (
        (1, '全国/多省/多市'),
        (2, '单省/单市'),
        (3, '项目'),
    )
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="客户名称")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="注册邮箱")
    password = models.CharField(max_length=200,  null=True, blank=True, verbose_name="密码")
    mobile_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="联系手机")
    level = models.SmallIntegerField(choices=user_level, verbose_name="角色")
    province = models.ForeignKey(to=Province, null=True, blank=True, verbose_name='省份', on_delete=models.CASCADE)
    elevators = models.TextField(null=True, blank=True, verbose_name="管理梯号")
    create_time = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"

    def __str__(self):
        return self.name
