# Generated by Django 3.1.1 on 2020-09-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsapp', '0003_auto_20200923_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdocument',
            name='slug',
            field=models.SlugField(default='slugislugslug', unique=True),
            preserve_default=False,
        ),
    ]