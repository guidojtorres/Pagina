# Generated by Django 3.0.3 on 2020-05-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20200521_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
