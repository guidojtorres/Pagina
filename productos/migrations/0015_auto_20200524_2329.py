# Generated by Django 3.0.3 on 2020-05-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_auto_20200524_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
