# Generated by Django 3.2.16 on 2022-12-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='sqft',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
