# Generated by Django 3.0.3 on 2020-05-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_auto_20200524_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(blank=True, choices=[('C', 'Carteras'), ('Z', 'Zapatos'), ('J', 'Jeans'), ('ZA', 'Zapatillas'), ('V', 'Vestidos'), ('A', 'Accesorios'), ('B', 'Botas')], max_length=15, null=True),
        ),
    ]
