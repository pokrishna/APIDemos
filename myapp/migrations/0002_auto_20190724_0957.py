# Generated by Django 2.2.3 on 2019-07-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='passw',
            field=models.CharField(default='india', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='rpass',
            field=models.CharField(default='ddd', max_length=40),
            preserve_default=False,
        ),
    ]
