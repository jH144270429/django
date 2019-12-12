# Generated by Django 2.2.7 on 2019-12-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='用户名'),
        ),
    ]
