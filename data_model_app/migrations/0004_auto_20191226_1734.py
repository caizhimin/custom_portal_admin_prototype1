# Generated by Django 2.1 on 2019-12-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_app', '0003_auto_20191226_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '全国/多省/多市'), (2, '单省/单市'), (3, '项目')], verbose_name='角色'),
        ),
    ]
